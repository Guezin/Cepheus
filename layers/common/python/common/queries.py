past_launches_query = """
{
  launchesPast {
    mission_name
    details
    launch_success
    launch_date_utc
    rocket {
      rocket {
        name
        cost_per_launch
        description
      }
    }
  }
}
"""