import add_json
import generate

category = 'あいさつ'
button_name = '안녕하세요'
add_json.update_json_data(category, button_name)
generate.generate()