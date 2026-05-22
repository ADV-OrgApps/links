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
        "my_school_of_nursing_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/4ca20025-81f3-47ba-a2e9-d7f9fcce8bc8?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_gift_records_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/5e1d56d2-e1df-4dea-891a-3d0c59010581?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_communications_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/1f529e00-9e5b-4728-ac61-8d1eee3669fd?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_donor_relations_insights": "https://app.fabric.microsoft.com/groups/27346895-48f2-4fec-8009-9057dd75366a/orgapps/76046300-e022-49f1-b530-634e8fc4f4b2?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_annual_giving_insights": "https://app.fabric.microsoft.com/groups/e7c5d421-a65f-4bd6-a19e-0ea72a517566/orgapps/65d21fc5-7b47-4241-8b30-d46da930b7b4?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_corporate_foundation_relations_insights": "https://app.fabric.microsoft.com/groups/e7c5d421-a65f-4bd6-a19e-0ea72a517566/orgapps/be2d05d1-cfe9-40ce-8915-a75a9e9f1daf?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_planned_giving_insights": "https://app.fabric.microsoft.com/groups/e7c5d421-a65f-4bd6-a19e-0ea72a517566/orgapps/7e6bb243-90e8-48ef-8df1-a95bf1ea6361?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_prospect_research_insights": "https://app.fabric.microsoft.com/groups/e7c5d421-a65f-4bd6-a19e-0ea72a517566/orgapps/0c3ffa31-bbf5-4899-9f97-6c34d92edd9d?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_alumni_insights": "https://app.fabric.microsoft.com/groups/e7c5d421-a65f-4bd6-a19e-0ea72a517566/orgapps/2f586bc6-271c-4966-bab8-6a5b721a4160?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c",
        "my_regional_development_insights": "https://app.fabric.microsoft.com/groups/e7c5d421-a65f-4bd6-a19e-0ea72a517566/orgapps/55a4f476-e3a6-4a82-af0a-f8b2938880bf?ctid=d8999fe4-76af-40b3-b435-1d8977abc08c"
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
