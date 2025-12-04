import sqlite3
with open('queries.sql', 'r', encoding='utf-8') as f:
    sql = f.read()
# Удаляем строки-комментарии, начинающиеся с '#', чтобы sqlite3 не ругался
sanitized = '\n'.join(l for l in sql.splitlines() if not l.lstrip().startswith('#'))
conn = sqlite3.connect('school.db')
conn.executescript(sanitized)
conn.commit()
conn.close()
print('Создан school.db на основе queries.sql (удалены #-комментарии)')
