import add_json
import generate

category = 'モノマネ'
button_name = 'どこでもドア'
add_json.update_json_data(category, button_name)
generate.generate()