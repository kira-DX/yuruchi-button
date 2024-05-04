import add_json
import generate

category = 'あいさつ'
button_name = 'へ～いわっつあっぷ'
add_json.update_json_data(category, button_name)
generate.generate()