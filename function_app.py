import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="go/{report_name}")
def link_redirect(req: func.HttpRequest) -> func.HttpResponse:
    # Capture the requested report from the URL
    report_name = req.route_params.get('report_name')

    # Dictionary mapping your clean URLs to the Fabric Org App GUIDs
    redirect_map = {
        # Annual Reports
        "digital_annual_report": "https://app.fabric.microsoft.com/groups/me/orgapps/c994d0ee-cdd9-43d3-8892-59ff978b3621?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "mobile_annual_report": "https://app.fabric.microsoft.com/groups/me/orgapps/4c8b1742-8ce8-41b2-ab71-384bb0626d43?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "print_annual_report": "https://app.fabric.microsoft.com/groups/me/orgapps/93c11ebb-fbff-46c1-b10b-34870726350d?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "static_digital_annual_report": "https://app.fabric.microsoft.com/groups/me/orgapps/04811eda-41d2-4bb7-b6b3-c65d1bedbc71?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        # Functional Areas Report Hubs
            # Test
        "my_school_of_nursing_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/4ca20025-81f3-47ba-a2e9-d7f9fcce8bc8?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
            # Batch 1
        "my_gift_records_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/5e1d56d2-e1df-4dea-891a-3d0c59010581?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
            # Batch 2
        "my_communications_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/1f529e00-9e5b-4728-ac61-8d1eee3669fd?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_donor_relations_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/76046300-e022-49f1-b530-634e8fc4f4b2?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
            # Batch 3
        "my_annual_giving_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/d6fb8dde-3ba1-47ab-9288-3caa43ff95d3?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_corporate_foundation_relations_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/1ca68847-5b7d-4117-89d3-97bef19d76f6?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_planned_giving_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/d3b56859-fd8a-4b1d-bd06-0e4f2fca8757?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_prospect_research_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/21b7adf7-7ef9-4df4-bd91-9e1b36aa14bf?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_alumni_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/1d01e4ab-ca90-4094-a756-0b6f68b89eb9?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_regional_development_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/77c7d90a-095e-4662-ab0e-cc14d7fdc457?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c"
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
