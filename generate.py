from dominate.tags import *
import dominate
import json

def generate():
    with open("api/static/text/description.json","r",encoding="utf-8") as file:
        description = json.load(file)
    with open("api/static/text/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    doc = dominate.document(title=description["title"])
    with doc:
        html(lang="ja")

    with doc.head:
        meta(charset="utf-8")
        meta(name="google-site-verification",content="fsRhq_lprbn64PdLt3miBwpUTYLT7Y2Je7UE-4ZI3r8")
        meta(name="description",content=description['description'])
        meta(name="viewport",content="width=device-width,initial-scale=1")
        link(rel="shortcut icon", type="image/x-icon", href="{{ url_for('static', filename='favicon.ico') }}")
        link(rel="stylesheet", type="text/css",href="{{ url_for('static', filename='css/style.css') }}")
        link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css")
        script(src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")
        script(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js")
        script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js")

    with doc.body:
        script(type="text/javascript", src="{{ url_for('static', filename='js/script.js') }}")
        with div(cls="main-app"):
            with div(cls="navbar navbar-dark fixed-top"):
                with div(cls="container-fluid",id="navbar_container"):
                    with button (cls="navbar-toggler", type="button", data_bs_toggle="offcanvas", data_bs_target="#offcanvasNavbar", aria_controls="offcanvasNavbar", aria_label="Toggle navigation"):
                        span (cls="navbar-toggler-icon")
                    a(description["site-title"], cls="navbar-brand",id="site-title", href="#")
                    
                    with div(cls="nav-item dropdown"):
                        a(description["default-lang"],id="default-lang", cls="nav-link navbar-brand dropdown-toggle", role="button", data_bs_toggle="dropdown", aria_expanded="false")
                        with ul(cls="dropdown-menu dropdown-menu-end"):
                            for lang_id,lang_name in description["lang"].items():
                                with li():
                                    a(lang_name,id=lang_id, cls="dropdown-item lang-switch",data_lang=lang_id)
                    
                    with div(cls="offcanvas offcanvas-start text-bg-dark",
                                tabindex="_1",
                                id="offcanvasNavbar",
                                aria_labelledby="SidebarLabel"):
                        with div(cls="offcanvas-header"):
                            with button(type="button",
                                    cls="navbar-toggler",
                                    data_bs_dismiss="offcanvas",
                                    aria_label="Close"):
                                span(cls="navbar-toggler-icon")
                            div(description["offcanvas-title"], cls="offcanvas-title", id="offcanvas-title")

                        with div(cls="offcanvas-body"):
                            with div(cls="options"):
                                input_(cls="repeat-check",type="checkbox", value="", id="flexCheckChecked",checked="")
                                label(description["voice_pause"],cls="form-check-label",_for="flexCheckChecked",id="voice_pause")
                            with ul(cls="navbar-nav flex-grow-1 pe-3",id="links"):
                                with li(cls="nav-item"):
                                    for site_id,site_info in description["links"].items():
                                        a(site_info[0],id=site_id, cls="nav-link", href=site_info[1],target="-blank")
                
            with div(cls="container-fluid",id="container_area"):
                for category_tag,(category, buttons) in enumerate(data.items()):
                    with div():
                        div(category,cls="category_area",id="category_{}".format(category_tag+1))
                        with div(cls="row"):
                            with div(cls="cate-body"):
                                for button_tag,button_name in enumerate(buttons):
                                    name,url = button_name.popitem()
                                    button(name,id="{}-{:03d}".format(category_tag+1,button_tag+1),**{"data-audio":"{}-{:03d}.mp3".format(category_tag+1,button_tag+1)},type="button", cls="btn btn-danger play-audio")
                                    
            with div(cls="container-fluid footer-custom", id="page-footer"):
                with div(cls="row",id='footer'):
                    with div(cls="col-md-6"):
                        p(description["footer_left"],id='footer_left')
                    with div(cls="col-md-6 text-end"):
                        p(description["declaration"],id="declaration")
                        for item_id,item_info in description["source"].items():
                            a(item_info[0],cls='sources',href=item_info[1],id=item_id,target="-blank")
                
            
    with open("api/templates/index.html","w",encoding="utf_8") as file:
        file.write(doc.render())