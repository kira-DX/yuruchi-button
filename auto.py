import add_json
import generate

category = 'その他'
button_name = '目覚ましボイス'
add_json.update_json_data(category, button_name)
generate.generate()