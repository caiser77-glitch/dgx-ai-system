# 문서당 청크 수를 최소화하여 데이터 밀도를 높이는 재구축 스크립트입니다.
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def rebuild_dense_db():
    source_dir = Path('~/AI_BASE/03_Processed_Data/Papers_Markdown').expanduser()
    db_dir = Path('~/AI_BASE/03_Processed_Data/Vector_DB').expanduser()
    
    print(f"🚀 고밀도 데이터베이스 재구축 시작: {source_dir} -> {db_dir}")

    # 1. 데이터 로드
    documents = []
    if not source_dir.exists():
        print(f"❌ 오류: {source_dir} 경로가 존재하지 않습니다.")
        return

    all_files = list(source_dir.glob("*.md"))
    print(f"📂 {len(all_files)}개의 파일을 로드 중입니다...")
    
    for file_path in all_files:
        try:
            loader = TextLoader(str(file_path), encoding="utf-8")
            documents.extend(loader.load())
        except Exception as e:
            print(f"⚠️ {file_path.name} 로드 실패: {e}")
            continue

    if not documents:
        print("❌ 로드된 문서가 없습니다.")
        return

    # 2. [핵심] 청크 사이즈 대폭 확대 (Density Optimization)
    # 문서를 아주 큰 단위로 쪼개어 청크 개수를 줄입니다.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,  # 청크 크기를 대폭 키움
        chunk_overlap=200 # 중복을 최소화함
    )
    splits = text_splitter.split_documents(documents)
    print(f"✅ {len(documents)}개 문서에서 {len(splits)}개의 밀도 높은 청크를 생성했습니다.")

    # 3. 임베딩 모델 로드
    print("🧠 임베딩 모델을 로드 중입니다 (시간이 소요될 수 있습니다)...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4. DB 생성 및 저장
    print("💾 고밀도 벡터 데이터베이스를 생성 중입니다...")
    
    # 기존 DB가 있다면 삭제 후 재생성을 권장 (사용자가 이미 rm -rf로 삭제했을 수 있음)
    vectorstore = Chroma.from_documents(
        documents=splits, 
        embedding=embeddings, 
        persist_directory=str(db_dir)
    )
    
    # ChromaDB 버전에 따라 자동 저장되지만 명시적으로 호출
    vectorstore.persist()

    print("\n" + "="*30)
    print(f"✅ 재구축 완료!")
    print(f" - 최종 청크 수: {len(splits)}개")
    print("="*30)
    print("💡 이제 더 넓은 맥락을 가진 데이터를 기반으로 분석할 준비가 되었습니다.")

if __name__ == "__main__":
    rebuild_dense_db()
