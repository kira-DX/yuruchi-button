import add_json
import generate

category = '奇声'
button_name = 'パパ、パパ、パァ〜'
add_json.update_json_data(category, button_name)
generate.generate()