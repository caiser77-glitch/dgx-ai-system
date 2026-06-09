# [최종] 오타를 완벽히 제거한 주제 분석 스크립트입니다.
from pathlib import Path
from collections import Counter
import re
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def analyze_top_topics():
    # 1. 경로 설정
    db_dir = Path('~/AI_BASE/03_Processed_data/Vector_DB').expanduser()
    # 만약 위 경로가 안된다면 사용자님의 실제 경로를 확인해야 합니다.
    if not db_dir.exists():
        db_dir = Path('~/AI_BASE/03_Processed_Data/Vector_DB').expanduser()
    
    print(f"🔍 데이터베이스 분석 시작: {db_dir}")

    try:
        # 2. 임베딩 모델 로드 (정확한 클래스명 사용)
        print("🧠 임베딩 모델을 로드 중입니다...")
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        # 위 줄에서 오타가 발생할 수 있으므로, 가장 확실한 클래스명으로 다시 정의합니다.
        from langchain_community.embeddings import HuggingFaceEmbeddings as HF
        embeddings = HF(model_name="sentence-transformers/all-MiniLM-L6-v2")

        # 3. ChromaDB 로드
        print("📂 데이터베이스를 연결 중입니다...")
        vectorstore = Chroma(persist_directory=str(db_dir), embedding_function=embeddings)
        
        # 4. 데이터 개수 확인 (SQL 변수 제한 오류 방지)
        print("🔍 데이터베이스 스캔 중...")
        total_count = vectorstore._collection.count()
        print(f"✅ 총 {total_count}개의 청크를 발견했습니다.")

        # 5. 키워드 카운터 설정
        word_counts = Counter()

        print(f"🚀 분석을 시작합니다. (Batch-based Scanning)")

        # 6. 데이터 추출 및 분석 루프
        batch_size = 100 
        for i in range(0, total_count, batch_size):
            try:
                # 데이터 가져오기 시도
                result = vectorstore.get(limit=batch_size, offset=i)
                
                if not result['documents']:
                    break
                
                for text in result['documents']:
                    # 한글/영문 단어 추출 (2글자 이상)
                    words = re.findall(r'[a-zA-Z가-힣]{2,}', text)
                    # 불용어 필터링 (강력한 리스트)
                    for w in words:
                        low_w = w.lower()
                        if len(low_w) > 2 and low_w not in {
                            'the', 'and', 'for', 'with', 'that', 'this', 'from', 'were', 'was', 
                            'are', 'has', 'have', 'but', 'not', 'which', 'they', 'their', 
                            'these', 'been', 'into', 'such', 'your', 'can', 'could', 
                            'should', 'would', 'will', 'shall', 'may', 'might',
                            'study', 'research', 'paper', 'using', 'based', 'analysis', 
                            'data', 'also', 'very', 'more', 'some', 'many', 'much', 
                            'used', 'used_to'
                        }:
                            word_counts[low_w] += 1

                print(f"   - {min(i + batch_size, total_count)} / {total_count} 완료...")

            except Exception as e:
                print(f"⚠️ 오류 발생: {e}")
                break

        # 7. 결과 출력
        print("\n" + "="*40)
        print("📊 [최종 결과] 핵심 주제 TOP 10")
        print("="*40)
        
        top_10 = word_counts.most_common(10)
        
        if not top_10:
            print("⚠️ 추출된 키워드가 없습니다. 데이터 양을 확인하세요.")
        else:
            for i, (word, count) in enumerate(top_10, 1):
                print(f"{i}. {word.upper()}: {count}회 언급")
        
        print("="*40)
        print(f"✅ 분석 완료. 총 {total_count}개 청크 처리됨.")

    except Exception as e:
        print(f"❌ 치명적 오류 발생: {e}")

if __name__ == "__main__":
    analyze_top_topics()
