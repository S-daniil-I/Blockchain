import json
import os
import hashlib

def get_blockchain_dir():
    return os.curdir + '/blocks/'

def get_sorted_files(blockchain_dir):
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])
    return files

def get_hash(filename):
    blockchain_dir = get_blockchain_dir()
    try:
        with open(blockchain_dir + filename, "rb") as file:
            file_content = file.read()
        return hashlib.sha256(file_content).hexdigest()
    except FileNotFoundError:
        return None

def check_integrity():
    blockchain_dir = get_blockchain_dir()
    files = get_sorted_files(blockchain_dir)
    results = []
    corruption_detected = False

    if not files:
        return results  # Нет блоков для проверки

    for i in range(1, len(files)):
        current_file = str(files[i])
        previous_file = str(files[i - 1])

        try:
            with open(blockchain_dir + current_file) as f:
                current_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            res = {'message': f'Ошибка при чтении блока {current_file}!', 'file': current_file}
            results.append(res)
            corruption_detected = True
            continue

        actual_prev_hash = get_hash(previous_file)

        if corruption_detected or current_data.get('hash') != actual_prev_hash:
            res = {'message': 'Блок поврежден!', 'file': current_file}  # Проверяем текущий блок
            corruption_detected = True
        else:
            res = {'message': 'Все хорошо. Никаких изменений не найдено.', 'file': current_file}  # Проверяем текущий блок

        results.append(res)

    # Проверка генезис-блока (если он есть и не является единственным)
    if len(files) > 1:
        genesis_file = str(files[0])
        try:
            with open(blockchain_dir + genesis_file) as f:
                genesis_data = json.load(f)
            results.insert(0, {'message': 'Генезис-блок проверен.', 'file': genesis_file})
        except (FileNotFoundError, json.JSONDecodeError):
            results.insert(0, {'message': f'Ошибка при чтении генезис-блока {genesis_file}!', 'file': genesis_file})

    return results

def write_block(name, amount, to_whom, prev_hash=''):
    blockchain_dir = get_blockchain_dir()
    files = get_sorted_files(blockchain_dir)

    if not files:
        filename = '1'  # Первый блок
        prev_hash = ''
    else:
        prev_file = files[-1]
        filename = str(prev_file + 1)
        prev_hash = get_hash(str(prev_file))

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}
    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print(check_integrity())

if __name__ == '__main__':
    main()