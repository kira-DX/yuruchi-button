import add_json
import generate

category = 'キレ芸'
button_name = 'そのまま沈んでろ！'
add_json.update_json_data(category, button_name)
generate.generate()