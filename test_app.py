import chromedriver_autoinstaller

from app import app


# Automatically install matching ChromeDriver
chromedriver_autoinstaller.install()


# Test Header
def test_header_present(dash_duo):

    dash_duo.start_server(app)

    header = dash_duo.find_element("#header")

    assert header.text == "Soul Foods Sales Dashboard"


# Test Graph
def test_graph_present(dash_duo):

    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")

    assert graph is not None


# Test Region Selector
def test_region_selector_present(dash_duo):

    dash_duo.start_server(app)

    selector = dash_duo.find_element("#region-selector")

    assert selector is not None