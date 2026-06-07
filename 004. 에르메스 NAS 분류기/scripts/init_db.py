import sqlite3
import os
from pathlib import Path

def main():
    db_dir = Path("/home/caiser77/dgx_workspace/004. 에르메스 NAS 분류기/data")
    db_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / "aurum_nas_rules.db"

    print(f"Initializing database at: {db_path}")
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS aurum_nas_rules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_name TEXT NOT NULL,
        original_path TEXT NOT NULL,
        inferred_class TEXT,
        user_approved_class TEXT,
        user_instruction TEXT,
        feedback_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # FTS5 가상 테이블 생성 (FTS5 활성화 여부와 관계없이 생성 시도)
    try:
        cursor.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS aurum_nas_rules_fts USING fts5(
            user_instruction,
            original_path,
            content='aurum_nas_rules'
        );
        """)
    except sqlite3.OperationalError as e:
        print(f"Warning: FTS5 virtual table creation failed ({e}). Proceeding without FTS5.")

    conn.commit()
    conn.close()
    print("Database initialization completed successfully!")

if __name__ == "__main__":
    main()
