import os

def generate_tree(startpath, indent='', file=None):
    """
    ディレクトリ構造を生成し、画面表示とファイル書き込みを同時に行う
    """
    if not os.path.exists(startpath):
        msg = f"Error: {startpath} は見つかりませんでした。"
        print(msg)
        if file: file.write(msg + '\n')
        return

    items = sorted(os.listdir(startpath))
    
    for i, item in enumerate(items):
        # 除外したいフォルダ・ファイル
        if item in ['.git', '__pycache__', '.DS_Store', 'node_modules']:
            continue
            
        path = os.path.join(startpath, item)
        is_last = (i == len(items) - 1)
        connector = '└── ' if is_last else '├── '
        
        line = f"{indent}{connector}{item}"
        print(line)
        if file:
            file.write(line + '\n')
        
        if os.path.isdir(path):
            new_indent = indent + ('    ' if is_last else '│   ')
            generate_tree(path, new_indent, file)

# --- 設定と実行 ---
target_dir = '.'  # 解析したいフォルダ
output_file = 'directory_structure.txt'

print(f"Scanning: {os.path.abspath(target_dir)}")
print("-" * 30)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(f"Directory tree for: {os.path.abspath(target_dir)}\n\n")
    generate_tree(target_dir, file=f)

print("-" * 30)
print(f"結果を {output_file} に保存しました。")