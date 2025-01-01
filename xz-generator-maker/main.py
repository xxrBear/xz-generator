import json
import os
import shutil

from jinja2 import Environment, FileSystemLoader

import utils

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
        env = Environment(loader=FileSystemLoader(r'E:\project\xz-generator\xz-generator-maker\resource\commands'))
        template = env.get_template('generate.py-tpl')
        output = template.render(meta_data)

        # generate.py的位置
        g_path = os.path.join(dest_path, 'commands/generate.py')
        with open(g_path, 'w', encoding='utf8') as f:
            f.write(output)
            os.remove(os.path.join(dest_path, 'commands/generate.py-tpl'))

if __name__ == '__main__':
    copy_content()
