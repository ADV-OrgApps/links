import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="go/{report_name}")
def link_redirect(req: func.HttpRequest) -> func.HttpResponse:
    # Capture the requested report from the URL
    report_name = req.route_params.get('report_name')

    # Dictionary mapping your clean URLs to the Fabric Org App GUIDs
    redirect_map = {
        "Digital_Annual_Report": "https://app.fabric.microsoft.com/groups/me/orgapps/c994d0ee-cdd9-43d3-8892-59ff978b3621?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "Mobile_Annual_Report": "https://app.fabric.microsoft.com/groups/me/orgapps/4c8b1742-8ce8-41b2-ab71-384bb0626d43?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "Print_Annual_Report": "https://app.fabric.microsoft.com/groups/me/orgapps/93c11ebb-fbff-46c1-b10b-34870726350d?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "Static_Digital_Annual_Report": "https://app.fabric.microsoft.com/groups/me/orgapps/04811eda-41d2-4bb7-b6b3-c65d1bedbc71?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c"
    }

    # Fetch the destination URL
    destination_url = redirect_map.get(report_name.lower())

    if destination_url:
        return func.HttpResponse(
            status_code=302,
            headers={"Location": destination_url}
        )
    else:
        return func.HttpResponse(
            "Report not found. Please verify the link.",
            status_code=404
        )
