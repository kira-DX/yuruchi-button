import add_json
import generate

category = 'ＩＱ３'
button_name = '褒めるな！褒めてほしい'
add_json.update_json_data(category, button_name)
generate.generate()