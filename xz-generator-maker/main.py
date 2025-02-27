import json
import os
import shutil

from jinja2 import Environment, FileSystemLoader


def handle_temp_file(env, meta_data, dest_path, file_path):
    template = env.get_template(file_path)

    output = template.render(meta_data)
    # 待处理文件的位置
    g_path = os.path.join(dest_path, file_path)

    # 删除模板文件
    with open(g_path.replace('-tpl', ''), 'w', encoding='utf8') as f:
        f.write(output)
        os.remove(os.path.join(dest_path, file_path))


def copy_content():
    with open('meta.json', 'r', encoding='utf8') as f:
        meta_data = json.loads(f.read())
    # print(meta_data)

    if meta_data:
        dest_path = meta_data.get('fileConfig').get('outputRootPath')
        input_path = meta_data.get('fileConfig').get('inputRootPath')

        try:
            # 如果目标文件夹不存在，则创建
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)

            # 使用 shutil.copytree 复制整个文件夹
            shutil.copytree(input_path, dest_path, dirs_exist_ok=True)  # Python 3.8+
            print(f"已成功复制 {input_path} 到 {dest_path}")
        except Exception as e:
            print(f"复制文件夹时出错: {e}")

        # 替换模板内容
        env = Environment(loader=FileSystemLoader('./resource'))
        handle_temp_file(env, meta_data, dest_path, 'commands/generate.py-tpl')
        handle_temp_file(env, meta_data, dest_path, 'README.md-tpl')


if __name__ == '__main__':
    copy_content()
