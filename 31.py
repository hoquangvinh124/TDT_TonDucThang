ex = input("Vui long nhap url: ")

def split_components(url):
    after_split = url.split('/')
    query_parameter = after_split[4].split('?', 1) if len(after_split) > 3 else ''
    if query_parameter:
        query_parameter[0] += '?'
    protocol = after_split[0]
    hostname = after_split[2]
    directory = after_split[3] if len(after_split) > 3 else ''
    file_name = query_parameter[0] if query_parameter else ''
    query_parameters = query_parameter[1] if len(query_parameter) > 1 else ''
    return (print(f'protocol: {protocol}'), print(f'hostname: {hostname}'), print(f'directory: {directory}')
            , print(f'file_name: {file_name}'), print(f'query_parameters: {query_parameters}'))

split_components(ex)





