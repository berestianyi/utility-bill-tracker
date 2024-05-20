from django.shortcuts import render


def chart(request):
    user_data_2020 = [
        {"label": "JAN", "y": 58200},
        {"label": "FEB", "y": 59110},
        {"label": "MAR", "y": 60320},
        {"label": "APR", "y": 61440},
        {"label": "MAY", "y": 62580},
        {"label": "JUN", "y": 63190},
        {"label": "JUL", "y": 64000},
        {"label": "AUG", "y": 64290},
        {"label": "SEP", "y": 65530},
        {"label": "OCT", "y": 65300},
        {"label": "NOV", "y": 65340},
        {"label": "DEC", "y": 64530},
    ]
    user_data_2021 = [
        {"label": "JAN", "y": 65100},
        {"label": "FEB", "y": 66210},
        {"label": "MAR", "y": 66540},
        {"label": "APR", "y": 66680},
        {"label": "MAY", "y": 67500},
        {"label": "JUN", "y": 68850},
        {"label": "JUL", "y": 69000},
        {"label": "AUG", "y": 70130},
        {"label": "SEP", "y": 71050},
        {"label": "OCT", "y": 71500},
        {"label": "NOV", "y": 72110},
        {"label": "DEC", "y": 71820},
    ]

    developer_work_week_data = [
        {"name": "Writing Code", "y": 30.7},
        {"name": "Debugging", "y": 36.4},
        {"name": "Problem Solving", "y": 3.7},
        {"name": "Firefighting", "y": 20.1},
        {"name": "Overhead", "y": 9.1}
    ]

    return render(
        request,
        "charts/statistic.html",
        {
            "user_data_2021": user_data_2021,
            "user_data_2020": user_data_2020,
            "developer_work_week_data": developer_work_week_data
        },
    )
