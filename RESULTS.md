-- Here are SQL answers and their outputs in app.
-- Some questions didn't ran at first so i added the questions in seed memory and then it worked.
-- There are some issue in output, it is not as you mentioned in assignment file like 
Response body:
{ "message": "Here are the top 5 patients by total spending...",
  "sql_query": "SELECT p.first_name, p.last_name, SUM(i.total_amount)...",
  "columns": ["first_name", "last_name", "total_spending"],
  "rows": [["John", "Smith", 4500], ["Jane", "Doe", 3200]],
  "row_count": 5,
  "chart": { "data": [...], "layout": {...} },
  "chart_type": "bar" }
 
 but in my output it is like {
  "message": "Here are the 7 results:",
  "sql_query": "SELECT strftime('%Y-%m', appointment_date) AS month, COUNT(*) AS count FROM appointments WHERE appointment_date >= date('now', '-6 months') GROUP BY month ORDER BY month",
  "columns": [
    "month",
    "count"
  ],
  "rows": [
    [
      "2025-10",
      33
    ],
    [
      "2025-11",
      39
    ],
    [
      "2025-12",
      38
    ],
    [
      "2026-01",
      41
    ],
    [
      "2026-02",
      41
    ],
    [
      "2026-03",
      41
    ],
    [
      "2026-04",
      9
    ]
  ],
  "row_count": 7,
  "chart": {
    "data": [
      {
        "name": "count",
        "x": [
          "2025-10",
          "2025-11",
          "2025-12",
          "2026-01",
          "2026-02",
          "2026-03",
          "2026-04"
        ],
        "y": [
          33,
          39,
          38,
          41,
          41,
          41,
          9
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "count by month"
      },
      "xaxis": {
        "title": {
          "text": "month"
        }
      },
      "yaxis": {
        "title": {
          "text": "count"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

--  I will figure this out and explain it in interview. 



1)How many patients do we have?
Response body

{
  "message": "Total count: 1",
  "sql_query": "SELECT COUNT(*) AS total_patients FROM patients",
  "columns": [
    "total_patients"
  ],
  "rows": [
    [
      200
    ]
  ],
  "row_count": 1,
  "chart": null,
  "chart_type": null,
  "error": null
}

2)List all doctors and their specializations
	
Response body

{
  "message": "Here are the 15 results:",
  "sql_query": "SELECT name, specialization, department FROM doctors ORDER BY specialization",
  "columns": [
    "name",
    "specialization",
    "department"
  ],
  "rows": [
    [
      "Dr. Reena Shah",
      "Cardiology",
      "Heart & Vascular"
    ],
    [
      "Dr. Ankit Malhotra",
      "Cardiology",
      "Heart & Vascular"
    ],
    [
      "Dr. Priti Nair",
      "Cardiology",
      "Heart & Vascular"
    ],
    [
      "Dr. Arun Kapoor",
      "Dermatology",
      "Skin Care"
    ],
    [
      "Dr. Meena Pillai",
      "Dermatology",
      "Skin Care"
    ],
    [
      "Dr. Sameer Joshi",
      "Dermatology",
      "Skin Care"
    ],
    [
      "Dr. Sunita Pandey",
      "General",
      "General Medicine"
    ],
    [
      "Dr. Vijay Mehta",
      "General",
      "General Medicine"
    ],
    [
      "Dr. Neha Gupta",
      "General",
      "General Medicine"
    ],
    [
      "Dr. Suresh Iyer",
      "Orthopedics",
      "Bone & Joint"
    ],
    [
      "Dr. Kavita Reddy",
      "Orthopedics",
      "Bone & Joint"
    ],
    [
      "Dr. Rahul Bose",
      "Orthopedics",
      "Bone & Joint"
    ],
    [
      "Dr. Rajesh Sharma",
      "Pediatrics",
      "Child Health"
    ],
    [
      "Dr. Divya Singh",
      "Pediatrics",
      "Child Health"
    ],
    [
      "Dr. Manish Verma",
      "Pediatrics",
      "Child Health"
    ]
  ],
  "row_count": 15,
  "chart": null,
  "chart_type": null,
  "error": null
}

3)Show me appointments for last month

{
  "message": "Here are the 7 results:",
  "sql_query": "SELECT strftime('%Y-%m', appointment_date) AS month, COUNT(*) AS count FROM appointments WHERE appointment_date >= date('now', '-6 months') GROUP BY month ORDER BY month",
  "columns": [
    "month",
    "count"
  ],
  "rows": [
    [
      "2025-10",
      33
    ],
    [
      "2025-11",
      39
    ],
    [
      "2025-12",
      38
    ],
    [
      "2026-01",
      41
    ],
    [
      "2026-02",
      41
    ],
    [
      "2026-03",
      41
    ],
    [
      "2026-04",
      9
    ]
  ],
  "row_count": 7,
  "chart": {
    "data": [
      {
        "name": "count",
        "x": [
          "2025-10",
          "2025-11",
          "2025-12",
          "2026-01",
          "2026-02",
          "2026-03",
          "2026-04"
        ],
        "y": [
          33,
          39,
          38,
          41,
          41,
          41,
          9
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "count by month"
      },
      "xaxis": {
        "title": {
          "text": "month"
        }
      },
      "yaxis": {
        "title": {
          "text": "count"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

4)Which doctor has the most appointments?
{
  "message": "Here are the 1 matching records:",
  "sql_query": "SELECT d.name, COUNT(a.id) AS appointment_count FROM doctors d JOIN appointments a ON a.doctor_id = d.id GROUP BY d.id, d.name ORDER BY appointment_count DESC LIMIT 1",
  "columns": [
    "name",
    "appointment_count"
  ],
  "rows": [
    [
      "Dr. Rahul Bose",
      55
    ]
  ],
  "row_count": 1,
  "chart": {
    "data": [
      {
        "name": "appointment_count",
        "x": [
          "Dr. Rahul Bose"
        ],
        "y": [
          55
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "appointment_count by name"
      },
      "xaxis": {
        "title": {
          "text": "name"
        }
      },
      "yaxis": {
        "title": {
          "text": "appointment_count"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

5)What is the total revenue?
{
  "message": "Found 1 result.",
  "sql_query": "SELECT SUM(total_amount) AS total_revenue FROM invoices",
  "columns": [
    "total_revenue"
  ],
  "rows": [
    [
      1193353.91
    ]
  ],
  "row_count": 1,
  "chart": null,
  "chart_type": null,
  "error": null
}

6)Show revenue by doctor
{
  "message": "Here are the 15 results:",
  "sql_query": "SELECT d.name, SUM(i.total_amount) AS total_revenue FROM invoices i JOIN appointments a ON a.patient_id = i.patient_id JOIN doctors d ON d.id = a.doctor_id GROUP BY d.name ORDER BY total_revenue DESC",
  "columns": [
    "name",
    "total_revenue"
  ],
  "rows": [
    [
      "Dr. Rahul Bose",
      340004.08
    ],
    [
      "Dr. Meena Pillai",
      317407.19
    ],
    [
      "Dr. Priti Nair",
      269729.04
    ],
    [
      "Dr. Kavita Reddy",
      258319.82
    ],
    [
      "Dr. Suresh Iyer",
      234910.35
    ],
    [
      "Dr. Divya Singh",
      213828.05
    ],
    [
      "Dr. Arun Kapoor",
      211752.63
    ],
    [
      "Dr. Sameer Joshi",
      186843.53
    ],
    [
      "Dr. Vijay Mehta",
      180926.65
    ],
    [
      "Dr. Sunita Pandey",
      160227.68
    ],
    [
      "Dr. Reena Shah",
      145775.42
    ],
    [
      "Dr. Neha Gupta",
      143608.65
    ],
    [
      "Dr. Manish Verma",
      84175.5
    ],
    [
      "Dr. Ankit Malhotra",
      57051.84
    ],
    [
      "Dr. Rajesh Sharma",
      43217.11
    ]
  ],
  "row_count": 15,
  "chart": {
    "data": [
      {
        "name": "total_revenue",
        "x": [
          "Dr. Rahul Bose",
          "Dr. Meena Pillai",
          "Dr. Priti Nair",
          "Dr. Kavita Reddy",
          "Dr. Suresh Iyer",
          "Dr. Divya Singh",
          "Dr. Arun Kapoor",
          "Dr. Sameer Joshi",
          "Dr. Vijay Mehta",
          "Dr. Sunita Pandey",
          "Dr. Reena Shah",
          "Dr. Neha Gupta",
          "Dr. Manish Verma",
          "Dr. Ankit Malhotra",
          "Dr. Rajesh Sharma"
        ],
        "y": [
          340004.08,
          317407.19,
          269729.04,
          258319.82,
          234910.35,
          213828.05,
          211752.63,
          186843.53,
          180926.65,
          160227.68,
          145775.42,
          143608.65,
          84175.5,
          57051.84,
          43217.11
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "total_revenue by name"
      },
      "xaxis": {
        "title": {
          "text": "name"
        }
      },
      "yaxis": {
        "title": {
          "text": "total_revenue"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

7)How many cancelled appointments last quarter?
{
  "message": "Total count: 120",
  "sql_query": "SELECT a.id, p.first_name, p.last_name, a.appointment_date, a.status FROM appointments a JOIN patients p ON p.id = a.patient_id WHERE a.status = 'Cancelled' ORDER BY a.appointment_date DESC",
  "columns": [
    "id",
    "first_name",
    "last_name",
    "appointment_date",
    "status"
  ],
  "rows": [
    [
      352,
      "Lata",
      "Malhotra",
      "2026-04-02 22:52:00",
      "Cancelled"
    ],
    [
      366,
      "Lata",
      "Patel",
      "2026-03-27 09:38:00",
      "Cancelled"
    ],
    [
      403,
      "Isha",
      "Kumar",
      "2026-03-24 19:41:00",
      "Cancelled"
    ],
    [
      153,
      "Swati",
      "Kapoor",
      "2026-03-22 16:59:00",
      "Cancelled"
    ],
    [
      441,
      "Riya",
      "Rao",
      "2026-03-17 19:12:00",
      "Cancelled"
    ],
    [
      30,
      "Rohan",
      "Das",
      "2026-03-16 08:57:00",
      "Cancelled"
    ],
    [
      494,
      "Manish",
      "Shah",
      "2026-03-11 18:53:00",
      "Cancelled"
    ],
    [
      148,
      "Manoj",
      "Malhotra",
      "2026-03-04 17:05:00",
      "Cancelled"
    ],
    [
      109,
      "Asha",
      "Kapoor",
      "2026-02-26 02:15:00",
      "Cancelled"
    ],
    [
      150,
      "Isha",
      "Nair",
      "2026-02-25 14:43:00",
      "Cancelled"
    ],
    [
      370,
      "Rajesh",
      "Das",
      "2026-02-23 03:44:00",
      "Cancelled"
    ],
    [
      367,
      "Suresh",
      "Shah",
      "2026-02-22 15:05:00",
      "Cancelled"
    ],
    [
      424,
      "Asha",
      "Verma",
      "2026-02-22 06:48:00",
      "Cancelled"
    ],
    [
      235,
      "Abhishek",
      "Mishra",
      "2026-02-19 19:41:00",
      "Cancelled"
    ],
    [
      29,
      "Naina",
      "Nair",
      "2026-02-17 15:36:00",
      "Cancelled"
    ],
    [
      131,
      "Suresh",
      "Mehta",
      "2026-02-08 02:52:00",
      "Cancelled"
    ],
    [
      83,
      "Yash",
      "Singh",
      "2026-02-07 10:20:00",
      "Cancelled"
    ],
    [
      107,
      "Pankaj",
      "Shah",
      "2026-02-07 02:22:00",
      "Cancelled"
    ],
    [
      165,
      "Vijay",
      "Bose",
      "2026-02-02 04:37:00",
      "Cancelled"
    ],
    [
      19,
      "Lata",
      "Iyer",
      "2026-02-02 01:52:00",
      "Cancelled"
    ],
    [
      398,
      "Dinesh",
      "Chopra",
      "2026-02-01 11:11:00",
      "Cancelled"
    ],
    [
      209,
      "Rajesh",
      "Das",
      "2026-02-01 03:01:00",
      "Cancelled"
    ],
    [
      56,
      "Harsh",
      "Rao",
      "2026-01-26 01:39:00",
      "Cancelled"
    ],
    [
      317,
      "Naina",
      "Kapoor",
      "2026-01-25 03:35:00",
      "Cancelled"
    ],
    [
      330,
      "Dinesh",
      "Verma",
      "2026-01-20 19:22:00",
      "Cancelled"
    ],
    [
      151,
      "Rahul",
      "Chopra",
      "2026-01-05 10:15:00",
      "Cancelled"
    ],
    [
      166,
      "Nikhil",
      "Verma",
      "2026-01-04 12:48:00",
      "Cancelled"
    ],
    [
      401,
      "Suresh",
      "Reddy",
      "2026-01-04 00:36:00",
      "Cancelled"
    ],
    [
      96,
      "Ankita",
      "Nair",
      "2025-12-31 21:37:00",
      "Cancelled"
    ],
    [
      300,
      "Arjun",
      "Pandey",
      "2025-12-31 01:31:00",
      "Cancelled"
    ],
    [
      389,
      "Arjun",
      "Pandey",
      "2025-12-22 14:05:00",
      "Cancelled"
    ],
    [
      36,
      "Pooja",
      "Rao",
      "2025-12-14 08:54:00",
      "Cancelled"
    ],
    [
      310,
      "Lata",
      "Mishra",
      "2025-12-13 22:13:00",
      "Cancelled"
    ],
    [
      171,
      "Abhishek",
      "Kapoor",
      "2025-12-06 17:43:00",
      "Cancelled"
    ],
    [
      246,
      "Suresh",
      "Shah",
      "2025-12-06 17:05:00",
      "Cancelled"
    ],
    [
      72,
      "Abhishek",
      "Mishra",
      "2025-12-05 13:36:00",
      "Cancelled"
    ],
    [
      25,
      "Pooja",
      "Rao",
      "2025-12-05 07:14:00",
      "Cancelled"
    ],
    [
      347,
      "Pankaj",
      "Kumar",
      "2025-12-04 10:57:00",
      "Cancelled"
    ],
    [
      122,
      "Manish",
      "Reddy",
      "2025-12-04 04:47:00",
      "Cancelled"
    ],
    [
      211,
      "Arjun",
      "Pandey",
      "2025-12-03 09:44:00",
      "Cancelled"
    ],
    [
      186,
      "Ananya",
      "Mishra",
      "2025-11-27 13:43:00",
      "Cancelled"
    ],
    [
      340,
      "Siddharth",
      "Malhotra",
      "2025-11-20 21:15:00",
      "Cancelled"
    ],
    [
      162,
      "Yash",
      "Reddy",
      "2025-11-14 17:35:00",
      "Cancelled"
    ],
    [
      196,
      "Rohan",
      "Sharma",
      "2025-11-13 21:08:00",
      "Cancelled"
    ],
    [
      48,
      "Abhishek",
      "Das",
      "2025-11-11 04:57:00",
      "Cancelled"
    ],
    [
      99,
      "Ayaan",
      "Mehta",
      "2025-11-07 14:30:00",
      "Cancelled"
    ],
    [
      328,
      "Aarav",
      "Nair",
      "2025-11-07 02:49:00",
      "Cancelled"
    ],
    [
      414,
      "Deepak",
      "Shah",
      "2025-11-01 06:13:00",
      "Cancelled"
    ],
    [
      257,
      "Rahul",
      "Kapoor",
      "2025-10-31 23:58:00",
      "Cancelled"
    ],
    [
      20,
      "Asha",
      "Malhotra",
      "2025-10-26 19:06:00",
      "Cancelled"
    ],
    [
      202,
      "Meera",
      "Nair",
      "2025-10-25 07:23:00",
      "Cancelled"
    ],
    [
      369,
      "Asha",
      "Kapoor",
      "2025-10-24 19:04:00",
      "Cancelled"
    ],
    [
      1,
      "Rohan",
      "Rao",
      "2025-10-20 09:42:00",
      "Cancelled"
    ],
    [
      88,
      "Ayaan",
      "Patel",
      "2025-10-17 03:17:00",
      "Cancelled"
    ],
    [
      216,
      "Sanjay",
      "Malhotra",
      "2025-10-12 11:06:00",
      "Cancelled"
    ],
    [
      480,
      "Asha",
      "Verma",
      "2025-10-11 07:25:00",
      "Cancelled"
    ],
    [
      433,
      "Kavita",
      "Iyer",
      "2025-10-08 14:30:00",
      "Cancelled"
    ],
    [
      154,
      "Ankita",
      "Bose",
      "2025-10-06 22:59:00",
      "Cancelled"
    ],
    [
      488,
      "Aarav",
      "Nair",
      "2025-10-04 03:08:00",
      "Cancelled"
    ],
    [
      206,
      "Aarav",
      "Reddy",
      "2025-10-03 22:40:00",
      "Cancelled"
    ],
    [
      337,
      "Meera",
      "Joshi",
      "2025-10-02 03:08:00",
      "Cancelled"
    ],
    [
      224,
      "Ankita",
      "Bose",
      "2025-09-27 19:11:00",
      "Cancelled"
    ],
    [
      304,
      "Rajesh",
      "Kapoor",
      "2025-09-23 10:31:00",
      "Cancelled"
    ],
    [
      66,
      "Divya",
      "Reddy",
      "2025-09-22 14:22:00",
      "Cancelled"
    ],
    [
      263,
      "Preeti",
      "Shah",
      "2025-09-21 22:27:00",
      "Cancelled"
    ],
    [
      219,
      "Riya",
      "Nair",
      "2025-09-18 11:11:00",
      "Cancelled"
    ],
    [
      312,
      "Manish",
      "Verma",
      "2025-09-18 06:37:00",
      "Cancelled"
    ],
    [
      90,
      "Naina",
      "Kapoor",
      "2025-09-17 05:32:00",
      "Cancelled"
    ],
    [
      267,
      "Suresh",
      "Kapoor",
      "2025-09-14 20:26:00",
      "Cancelled"
    ],
    [
      159,
      "Harsh",
      "Kapoor",
      "2025-09-12 01:00:00",
      "Cancelled"
    ],
    [
      499,
      "Vijay",
      "Pandey",
      "2025-09-11 12:40:00",
      "Cancelled"
    ],
    [
      124,
      "Rajesh",
      "Chopra",
      "2025-09-10 16:51:00",
      "Cancelled"
    ],
    [
      458,
      "Ayaan",
      "Mehta",
      "2025-09-08 07:42:00",
      "Cancelled"
    ],
    [
      406,
      "Preeti",
      "Nair",
      "2025-09-07 10:02:00",
      "Cancelled"
    ],
    [
      115,
      "Tanvi",
      "Bose",
      "2025-08-30 20:49:00",
      "Cancelled"
    ],
    [
      292,
      "Suresh",
      "Shah",
      "2025-08-23 08:25:00",
      "Cancelled"
    ],
    [
      321,
      "Rohan",
      "Das",
      "2025-08-19 23:52:00",
      "Cancelled"
    ],
    [
      123,
      "Asha",
      "Patel",
      "2025-08-19 05:42:00",
      "Cancelled"
    ],
    [
      93,
      "Riya",
      "Singh",
      "2025-08-18 09:47:00",
      "Cancelled"
    ],
    [
      118,
      "Rajesh",
      "Singh",
      "2025-08-16 19:54:00",
      "Cancelled"
    ],
    [
      47,
      "Rahul",
      "Mishra",
      "2025-08-15 06:36:00",
      "Cancelled"
    ],
    [
      220,
      "Varun",
      "Das",
      "2025-08-12 23:24:00",
      "Cancelled"
    ],
    [
      213,
      "Aditya",
      "Joshi",
      "2025-08-05 19:11:00",
      "Cancelled"
    ],
    [
      243,
      "Rahul",
      "Joshi",
      "2025-08-04 17:31:00",
      "Cancelled"
    ],
    [
      225,
      "Meera",
      "Nair",
      "2025-07-30 03:59:00",
      "Cancelled"
    ],
    [
      174,
      "Rahul",
      "Kapoor",
      "2025-07-28 00:52:00",
      "Cancelled"
    ],
    [
      101,
      "Deepak",
      "Shah",
      "2025-07-27 09:25:00",
      "Cancelled"
    ],
    [
      208,
      "Abhishek",
      "Mehta",
      "2025-07-23 16:36:00",
      "Cancelled"
    ],
    [
      252,
      "Pankaj",
      "Mishra",
      "2025-07-23 12:56:00",
      "Cancelled"
    ],
    [
      435,
      "Asha",
      "Iyer",
      "2025-07-22 05:12:00",
      "Cancelled"
    ],
    [
      60,
      "Preeti",
      "Iyer",
      "2025-07-18 17:05:00",
      "Cancelled"
    ],
    [
      388,
      "Rajesh",
      "Reddy",
      "2025-07-18 15:37:00",
      "Cancelled"
    ],
    [
      290,
      "Varun",
      "Das",
      "2025-07-17 12:12:00",
      "Cancelled"
    ],
    [
      260,
      "Dinesh",
      "Nair",
      "2025-07-10 11:23:00",
      "Cancelled"
    ],
    [
      21,
      "Preeti",
      "Mehta",
      "2025-07-04 14:15:00",
      "Cancelled"
    ],
    [
      69,
      "Ankita",
      "Bose",
      "2025-06-27 18:03:00",
      "Cancelled"
    ],
    [
      73,
      "Riya",
      "Nair",
      "2025-06-27 13:35:00",
      "Cancelled"
    ],
    [
      462,
      "Isha",
      "Nair",
      "2025-06-25 05:00:00",
      "Cancelled"
    ],
    [
      172,
      "Sunita",
      "Bose",
      "2025-06-23 20:49:00",
      "Cancelled"
    ],
    [
      140,
      "Abhishek",
      "Mishra",
      "2025-06-23 04:03:00",
      "Cancelled"
    ],
    [
      173,
      "Rohan",
      "Shah",
      "2025-06-22 10:07:00",
      "Cancelled"
    ],
    [
      149,
      "Vijay",
      "Bose",
      "2025-06-17 00:11:00",
      "Cancelled"
    ],
    [
      31,
      "Suresh",
      "Sharma",
      "2025-06-10 02:26:00",
      "Cancelled"
    ],
    [
      204,
      "Tara",
      "Sharma",
      "2025-06-07 22:30:00",
      "Cancelled"
    ],
    [
      420,
      "Manish",
      "Shah",
      "2025-06-07 07:53:00",
      "Cancelled"
    ],
    [
      283,
      "Deepak",
      "Iyer",
      "2025-06-06 15:41:00",
      "Cancelled"
    ],
    [
      342,
      "Asha",
      "Gupta",
      "2025-06-01 12:17:00",
      "Cancelled"
    ],
    [
      239,
      "Kavya",
      "Malhotra",
      "2025-05-31 13:55:00",
      "Cancelled"
    ],
    [
      195,
      "Vijay",
      "Chopra",
      "2025-05-30 00:15:00",
      "Cancelled"
    ],
    [
      7,
      "Pankaj",
      "Shah",
      "2025-05-26 23:58:00",
      "Cancelled"
    ],
    [
      71,
      "Arjun",
      "Das",
      "2025-05-26 16:57:00",
      "Cancelled"
    ],
    [
      87,
      "Geeta",
      "Pandey",
      "2025-05-20 05:48:00",
      "Cancelled"
    ],
    [
      53,
      "Kavya",
      "Malhotra",
      "2025-05-05 13:13:00",
      "Cancelled"
    ],
    [
      293,
      "Ankita",
      "Nair",
      "2025-05-01 21:26:00",
      "Cancelled"
    ],
    [
      264,
      "Shreya",
      "Verma",
      "2025-04-30 16:44:00",
      "Cancelled"
    ],
    [
      89,
      "Ananya",
      "Singh",
      "2025-04-27 14:27:00",
      "Cancelled"
    ],
    [
      237,
      "Manish",
      "Verma",
      "2025-04-18 05:44:00",
      "Cancelled"
    ],
    [
      495,
      "Sanjay",
      "Patel",
      "2025-04-18 00:39:00",
      "Cancelled"
    ],
    [
      467,
      "Vijay",
      "Chopra",
      "2025-04-16 18:16:00",
      "Cancelled"
    ],
    [
      349,
      "Harsh",
      "Rao",
      "2025-04-14 11:52:00",
      "Cancelled"
    ]
  ],
  "row_count": 120,
  "chart": {
    "data": [
      {
        "name": "id",
        "x": [
          352,
          366,
          403,
          153,
          441,
          30,
          494,
          148,
          109,
          150,
          370,
          367,
          424,
          235,
          29,
          131,
          83,
          107,
          165,
          19,
          398,
          209,
          56,
          317,
          330,
          151,
          166,
          401,
          96,
          300,
          389,
          36,
          310,
          171,
          246,
          72,
          25,
          347,
          122,
          211,
          186,
          340,
          162,
          196,
          48,
          99,
          328,
          414,
          257,
          20,
          202,
          369,
          1,
          88,
          216,
          480,
          433,
          154,
          488,
          206,
          337,
          224,
          304,
          66,
          263,
          219,
          312,
          90,
          267,
          159,
          499,
          124,
          458,
          406,
          115,
          292,
          321,
          123,
          93,
          118,
          47,
          220,
          213,
          243,
          225,
          174,
          101,
          208,
          252,
          435,
          60,
          388,
          290,
          260,
          21,
          69,
          73,
          462,
          172,
          140,
          173,
          149,
          31,
          204,
          420,
          283,
          342,
          239,
          195,
          7,
          71,
          87,
          53,
          293,
          264,
          89,
          237,
          495,
          467,
          349
        ],
        "y": [
          352,
          366,
          403,
          153,
          441,
          30,
          494,
          148,
          109,
          150,
          370,
          367,
          424,
          235,
          29,
          131,
          83,
          107,
          165,
          19,
          398,
          209,
          56,
          317,
          330,
          151,
          166,
          401,
          96,
          300,
          389,
          36,
          310,
          171,
          246,
          72,
          25,
          347,
          122,
          211,
          186,
          340,
          162,
          196,
          48,
          99,
          328,
          414,
          257,
          20,
          202,
          369,
          1,
          88,
          216,
          480,
          433,
          154,
          488,
          206,
          337,
          224,
          304,
          66,
          263,
          219,
          312,
          90,
          267,
          159,
          499,
          124,
          458,
          406,
          115,
          292,
          321,
          123,
          93,
          118,
          47,
          220,
          213,
          243,
          225,
          174,
          101,
          208,
          252,
          435,
          60,
          388,
          290,
          260,
          21,
          69,
          73,
          462,
          172,
          140,
          173,
          149,
          31,
          204,
          420,
          283,
          342,
          239,
          195,
          7,
          71,
          87,
          53,
          293,
          264,
          89,
          237,
          495,
          467,
          349
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "id by id"
      },
      "xaxis": {
        "title": {
          "text": "id"
        }
      },
      "yaxis": {
        "title": {
          "text": "id"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

8)Top 5 patients by spending
{
  "message": "Here are the 5 matching records:",
  "sql_query": "SELECT p.first_name, p.last_name, SUM(i.total_amount) AS total_spending FROM patients p JOIN invoices i ON i.patient_id = p.id GROUP BY p.id, p.first_name, p.last_name ORDER BY total_spending DESC LIMIT 5",
  "columns": [
    "first_name",
    "last_name",
    "total_spending"
  ],
  "rows": [
    [
      "Swati",
      "Mishra",
      30838.92
    ],
    [
      "Tara",
      "Pandey",
      26745.79
    ],
    [
      "Manish",
      "Malhotra",
      25243.04
    ],
    [
      "Aditya",
      "Kapoor",
      21157.510000000002
    ],
    [
      "Asha",
      "Verma",
      20050.23
    ]
  ],
  "row_count": 5,
  "chart": {
    "data": [
      {
        "name": "total_spending",
        "x": [
          "Swati",
          "Tara",
          "Manish",
          "Aditya",
          "Asha"
        ],
        "y": [
          30838.92,
          26745.79,
          25243.04,
          21157.510000000002,
          20050.23
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "total_spending by first_name"
      },
      "xaxis": {
        "title": {
          "text": "first_name"
        }
      },
      "yaxis": {
        "title": {
          "text": "total_spending"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

9)Average treatment cost by specialization
{
  "message": "Found 5 results.",
  "sql_query": "SELECT d.specialization, ROUND(AVG(t.cost), 2) AS avg_cost FROM treatments t JOIN appointments a ON a.id = t.appointment_id JOIN doctors d ON d.id = a.doctor_id GROUP BY d.specialization ORDER BY avg_cost DESC",
  "columns": [
    "specialization",
    "avg_cost"
  ],
  "rows": [
    [
      "Pediatrics",
      2679.41
    ],
    [
      "Cardiology",
      2564.58
    ],
    [
      "Orthopedics",
      2392.27
    ],
    [
      "General",
      2331.43
    ],
    [
      "Dermatology",
      2267.14
    ]
  ],
  "row_count": 5,
  "chart": {
    "data": [
      {
        "name": "avg_cost",
        "x": [
          "Pediatrics",
          "Cardiology",
          "Orthopedics",
          "General",
          "Dermatology"
        ],
        "y": [
          2679.41,
          2564.58,
          2392.27,
          2331.43,
          2267.14
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "avg_cost by specialization"
      },
      "xaxis": {
        "title": {
          "text": "specialization"
        }
      },
      "yaxis": {
        "title": {
          "text": "avg_cost"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

10)Show monthly appointment count for the past 6 months
{
  "message": "Total count: 7",
  "sql_query": "SELECT strftime('%Y-%m', appointment_date) AS month, COUNT(*) AS count FROM appointments WHERE appointment_date >= date('now', '-6 months') GROUP BY month ORDER BY month",
  "columns": [
    "month",
    "count"
  ],
  "rows": [
    [
      "2025-10",
      33
    ],
    [
      "2025-11",
      39
    ],
    [
      "2025-12",
      38
    ],
    [
      "2026-01",
      41
    ],
    [
      "2026-02",
      41
    ],
    [
      "2026-03",
      41
    ],
    [
      "2026-04",
      9
    ]
  ],
  "row_count": 7,
  "chart": {
    "data": [
      {
        "name": "count",
        "x": [
          "2025-10",
          "2025-11",
          "2025-12",
          "2026-01",
          "2026-02",
          "2026-03",
          "2026-04"
        ],
        "y": [
          33,
          39,
          38,
          41,
          41,
          41,
          9
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "count by month"
      },
      "xaxis": {
        "title": {
          "text": "month"
        }
      },
      "yaxis": {
        "title": {
          "text": "count"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

11) Which city has the most patients?
{
  "message": "Here are the 1 matching records:",
  "sql_query": "SELECT city, COUNT(*) AS patient_count FROM patients GROUP BY city ORDER BY patient_count DESC LIMIT 1",
  "columns": [
    "city",
    "patient_count"
  ],
  "rows": [
    [
      "Kolkata",
      25
    ]
  ],
  "row_count": 1,
  "chart": {
    "data": [
      {
        "name": "patient_count",
        "x": [
          "Kolkata"
        ],
        "y": [
          25
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "patient_count by city"
      },
      "xaxis": {
        "title": {
          "text": "city"
        }
      },
      "yaxis": {
        "title": {
          "text": "patient_count"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

12)List patients who visited more than 3 times
{
  "message": "Here are the 29 results:",
  "sql_query": "SELECT p.first_name, p.last_name, COUNT(a.id) AS visit_count FROM patients p JOIN appointments a ON a.patient_id = p.id GROUP BY p.id, p.first_name, p.last_name HAVING COUNT(a.id) > 3 ORDER BY visit_count DESC",
  "columns": [
    "first_name",
    "last_name",
    "visit_count"
  ],
  "rows": [
    [
      "Sunita",
      "Bose",
      8
    ],
    [
      "Pooja",
      "Rao",
      8
    ],
    [
      "Riya",
      "Nair",
      8
    ],
    [
      "Aarav",
      "Nair",
      7
    ],
    [
      "Ayaan",
      "Patel",
      7
    ],
    [
      "Suresh",
      "Shah",
      7
    ],
    [
      "Meera",
      "Nair",
      7
    ],
    [
      "Manish",
      "Verma",
      7
    ],
    [
      "Abhishek",
      "Mishra",
      7
    ],
    [
      "Rajesh",
      "Reddy",
      7
    ],
    [
      "Asha",
      "Kapoor",
      7
    ],
    [
      "Harsh",
      "Rao",
      7
    ],
    [
      "Asha",
      "Verma",
      7
    ],
    [
      "Arjun",
      "Pandey",
      6
    ],
    [
      "Vijay",
      "Chopra",
      6
    ],
    [
      "Suresh",
      "Reddy",
      6
    ],
    [
      "Varun",
      "Das",
      6
    ],
    [
      "Rahul",
      "Kapoor",
      6
    ],
    [
      "Manish",
      "Reddy",
      6
    ],
    [
      "Aarav",
      "Sharma",
      5
    ],
    [
      "Rahul",
      "Joshi",
      5
    ],
    [
      "Manoj",
      "Malhotra",
      5
    ],
    [
      "Rahul",
      "Mishra",
      5
    ],
    [
      "Isha",
      "Nair",
      5
    ],
    [
      "Dinesh",
      "Verma",
      5
    ],
    [
      "Naina",
      "Nair",
      5
    ],
    [
      "Kavya",
      "Malhotra",
      5
    ],
    [
      "Deepak",
      "Shah",
      5
    ],
    [
      "Vijay",
      "Verma",
      4
    ]
  ],
  "row_count": 29,
  "chart": {
    "data": [
      {
        "name": "visit_count",
        "x": [
          "Sunita",
          "Pooja",
          "Riya",
          "Aarav",
          "Ayaan",
          "Suresh",
          "Meera",
          "Manish",
          "Abhishek",
          "Rajesh",
          "Asha",
          "Harsh",
          "Asha",
          "Arjun",
          "Vijay",
          "Suresh",
          "Varun",
          "Rahul",
          "Manish",
          "Aarav",
          "Rahul",
          "Manoj",
          "Rahul",
          "Isha",
          "Dinesh",
          "Naina",
          "Kavya",
          "Deepak",
          "Vijay"
        ],
        "y": [
          8,
          8,
          8,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          6,
          6,
          6,
          6,
          6,
          6,
          5,
          5,
          5,
          5,
          5,
          5,
          5,
          5,
          5,
          4
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "visit_count by first_name"
      },
      "xaxis": {
        "title": {
          "text": "first_name"
        }
      },
      "yaxis": {
        "title": {
          "text": "visit_count"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

13)Show unpaid invoices
{
  "message": "Here are the 142 results:",
  "sql_query": "SELECT p.first_name, p.last_name, i.invoice_date, i.total_amount, i.paid_amount, i.status FROM invoices i JOIN patients p ON p.id = i.patient_id WHERE i.status IN ('Pending', 'Overdue') ORDER BY i.invoice_date DESC",
  "columns": [
    "first_name",
    "last_name",
    "invoice_date",
    "total_amount",
    "paid_amount",
    "status"
  ],
  "rows": [
    [
      "Kavya",
      "Mehta",
      "2026-03-29",
      461.47,
      70.13,
      "Pending"
    ],
    [
      "Amit",
      "Shah",
      "2026-03-28",
      606.39,
      93.74,
      "Overdue"
    ],
    [
      "Tanvi",
      "Bose",
      "2026-03-24",
      4584.72,
      1136.45,
      "Pending"
    ],
    [
      "Kavya",
      "Mehta",
      "2026-03-23",
      1625.88,
      634,
      "Pending"
    ],
    [
      "Harsh",
      "Rao",
      "2026-03-23",
      4872.22,
      732.1,
      "Pending"
    ],
    [
      "Suresh",
      "Kapoor",
      "2026-03-19",
      4640.06,
      756.67,
      "Overdue"
    ],
    [
      "Meera",
      "Nair",
      "2026-03-13",
      2112.88,
      0.71,
      "Pending"
    ],
    [
      "Ananya",
      "Mishra",
      "2026-03-11",
      708.78,
      138.04,
      "Overdue"
    ],
    [
      "Divya",
      "Das",
      "2026-03-05",
      417.22,
      64.14,
      "Pending"
    ],
    [
      "Yash",
      "Singh",
      "2026-03-02",
      5913.55,
      439,
      "Pending"
    ],
    [
      "Riya",
      "Nair",
      "2026-02-28",
      1600.16,
      29.92,
      "Overdue"
    ],
    [
      "Asha",
      "Malhotra",
      "2026-02-24",
      6337.03,
      1113.35,
      "Overdue"
    ],
    [
      "Tara",
      "Pandey",
      "2026-02-23",
      6230.14,
      176.74,
      "Overdue"
    ],
    [
      "Asha",
      "Verma",
      "2026-02-22",
      348.59,
      83.28,
      "Pending"
    ],
    [
      "Rajesh",
      "Kapoor",
      "2026-02-16",
      2792.2,
      38.21,
      "Overdue"
    ],
    [
      "Pankaj",
      "Kumar",
      "2026-02-12",
      1795.85,
      457.67,
      "Pending"
    ],
    [
      "Rajesh",
      "Singh",
      "2026-02-10",
      6373.16,
      2037.89,
      "Pending"
    ],
    [
      "Riya",
      "Nair",
      "2026-02-07",
      822.4,
      24.66,
      "Overdue"
    ],
    [
      "Asha",
      "Kapoor",
      "2026-02-07",
      2769.23,
      432.61,
      "Pending"
    ],
    [
      "Manoj",
      "Pandey",
      "2026-02-07",
      3200.69,
      588.55,
      "Overdue"
    ],
    [
      "Rekha",
      "Patel",
      "2026-02-02",
      3360.84,
      200.96,
      "Overdue"
    ],
    [
      "Abhishek",
      "Mishra",
      "2026-01-30",
      2955.07,
      1445.45,
      "Pending"
    ],
    [
      "Kavita",
      "Rao",
      "2026-01-28",
      6468.59,
      1549.66,
      "Overdue"
    ],
    [
      "Asha",
      "Verma",
      "2026-01-28",
      5862.7,
      1689.75,
      "Overdue"
    ],
    [
      "Manish",
      "Shah",
      "2026-01-21",
      1481.53,
      637.78,
      "Pending"
    ],
    [
      "Asha",
      "Verma",
      "2026-01-20",
      6984.07,
      3120.06,
      "Pending"
    ],
    [
      "Tara",
      "Shah",
      "2026-01-17",
      5524.87,
      29.42,
      "Overdue"
    ],
    [
      "Tara",
      "Shah",
      "2026-01-15",
      5202.75,
      470.38,
      "Overdue"
    ],
    [
      "Rekha",
      "Patel",
      "2026-01-13",
      1311.87,
      214.16,
      "Overdue"
    ],
    [
      "Vijay",
      "Bose",
      "2026-01-12",
      5485.59,
      894.89,
      "Pending"
    ],
    [
      "Amit",
      "Shah",
      "2026-01-10",
      828.17,
      138.75,
      "Pending"
    ],
    [
      "Ananya",
      "Mishra",
      "2025-12-31",
      6839.46,
      160.73,
      "Overdue"
    ],
    [
      "Naina",
      "Kapoor",
      "2025-12-25",
      7142.16,
      453.13,
      "Overdue"
    ],
    [
      "Siddharth",
      "Malhotra",
      "2025-12-23",
      5915.26,
      470.9,
      "Overdue"
    ],
    [
      "Manoj",
      "Pandey",
      "2025-12-21",
      6481.89,
      1675.41,
      "Pending"
    ],
    [
      "Aarav",
      "Nair",
      "2025-12-19",
      2042.58,
      311.73,
      "Pending"
    ],
    [
      "Manish",
      "Mishra",
      "2025-12-18",
      6014.27,
      2046.05,
      "Pending"
    ],
    [
      "Varun",
      "Das",
      "2025-12-15",
      1424.21,
      395.66,
      "Pending"
    ],
    [
      "Aditya",
      "Kapoor",
      "2025-12-14",
      5434.43,
      707.58,
      "Pending"
    ],
    [
      "Ankita",
      "Nair",
      "2025-12-10",
      6862.05,
      547.15,
      "Overdue"
    ],
    [
      "Rekha",
      "Mishra",
      "2025-12-08",
      1843.79,
      206.76,
      "Pending"
    ],
    [
      "Ayaan",
      "Bose",
      "2025-12-05",
      1125.29,
      271.72,
      "Pending"
    ],
    [
      "Lata",
      "Malhotra",
      "2025-12-04",
      1543.23,
      267.75,
      "Overdue"
    ],
    [
      "Meera",
      "Kumar",
      "2025-12-02",
      750.47,
      125.17,
      "Pending"
    ],
    [
      "Suresh",
      "Shah",
      "2025-12-01",
      7605.65,
      3443.72,
      "Pending"
    ],
    [
      "Ayaan",
      "Patel",
      "2025-12-01",
      702.57,
      222.37,
      "Pending"
    ],
    [
      "Swati",
      "Kapoor",
      "2025-11-28",
      2926.44,
      786.37,
      "Overdue"
    ],
    [
      "Rahul",
      "Joshi",
      "2025-11-27",
      6051.24,
      1183.52,
      "Overdue"
    ],
    [
      "Rajesh",
      "Singh",
      "2025-11-25",
      4877.21,
      1044.92,
      "Pending"
    ],
    [
      "Swati",
      "Bose",
      "2025-11-21",
      418.92,
      43.48,
      "Pending"
    ],
    [
      "Sanjay",
      "Patel",
      "2025-11-20",
      6464.26,
      29.84,
      "Overdue"
    ],
    [
      "Riya",
      "Singh",
      "2025-11-19",
      1427.85,
      382.8,
      "Pending"
    ],
    [
      "Riya",
      "Rao",
      "2025-11-18",
      6499.8,
      1166.12,
      "Overdue"
    ],
    [
      "Asha",
      "Verma",
      "2025-11-16",
      3749.65,
      641.57,
      "Overdue"
    ],
    [
      "Pooja",
      "Rao",
      "2025-11-15",
      1561.23,
      99.78,
      "Overdue"
    ],
    [
      "Isha",
      "Kumar",
      "2025-11-11",
      5492.56,
      1157.92,
      "Overdue"
    ],
    [
      "Manoj",
      "Malhotra",
      "2025-11-10",
      1509.14,
      84.03,
      "Pending"
    ],
    [
      "Usha",
      "Kapoor",
      "2025-11-05",
      3663.52,
      1200.75,
      "Pending"
    ],
    [
      "Siddharth",
      "Malhotra",
      "2025-11-05",
      4656.04,
      2314.27,
      "Pending"
    ],
    [
      "Divya",
      "Shah",
      "2025-11-01",
      4244.75,
      2096.49,
      "Pending"
    ],
    [
      "Pankaj",
      "Mishra",
      "2025-10-31",
      6464.24,
      3192.31,
      "Pending"
    ],
    [
      "Kavita",
      "Iyer",
      "2025-10-31",
      4217.27,
      878.03,
      "Overdue"
    ],
    [
      "Arjun",
      "Kumar",
      "2025-10-30",
      3317.49,
      681.33,
      "Pending"
    ],
    [
      "Ankita",
      "Chopra",
      "2025-10-30",
      7745.02,
      849.31,
      "Overdue"
    ],
    [
      "Kunal",
      "Singh",
      "2025-10-22",
      703.55,
      313.56,
      "Pending"
    ],
    [
      "Aditya",
      "Chopra",
      "2025-10-21",
      7608.31,
      538.16,
      "Overdue"
    ],
    [
      "Naina",
      "Nair",
      "2025-10-19",
      4060.96,
      1565.81,
      "Pending"
    ],
    [
      "Kavita",
      "Mehta",
      "2025-10-14",
      418.7,
      110.38,
      "Overdue"
    ],
    [
      "Harsh",
      "Rao",
      "2025-10-09",
      4527.36,
      2253.13,
      "Pending"
    ],
    [
      "Vijay",
      "Bose",
      "2025-10-04",
      4514.4,
      1211.91,
      "Pending"
    ],
    [
      "Riya",
      "Iyer",
      "2025-10-02",
      1498.82,
      588.51,
      "Pending"
    ],
    [
      "Manish",
      "Malhotra",
      "2025-10-01",
      729.15,
      197.39,
      "Overdue"
    ],
    [
      "Shreya",
      "Verma",
      "2025-09-29",
      6693.75,
      637.03,
      "Overdue"
    ],
    [
      "Ankita",
      "Chopra",
      "2025-09-27",
      5916.35,
      560.65,
      "Overdue"
    ],
    [
      "Amit",
      "Reddy",
      "2025-09-24",
      3520.36,
      1671.32,
      "Pending"
    ],
    [
      "Kavya",
      "Malhotra",
      "2025-09-24",
      5241.1,
      1926.04,
      "Pending"
    ],
    [
      "Varun",
      "Gupta",
      "2025-09-21",
      6362.39,
      367.45,
      "Pending"
    ],
    [
      "Vijay",
      "Verma",
      "2025-09-12",
      657.06,
      42.1,
      "Overdue"
    ],
    [
      "Ayaan",
      "Bose",
      "2025-09-12",
      4660.02,
      1479.24,
      "Pending"
    ],
    [
      "Preeti",
      "Iyer",
      "2025-09-12",
      2675.64,
      550.01,
      "Overdue"
    ],
    [
      "Kunal",
      "Rao",
      "2025-09-09",
      5442.88,
      52.23,
      "Overdue"
    ],
    [
      "Naina",
      "Kapoor",
      "2025-09-05",
      6373.45,
      727.48,
      "Overdue"
    ],
    [
      "Kunal",
      "Singh",
      "2025-09-03",
      3446.59,
      743.9,
      "Overdue"
    ],
    [
      "Pankaj",
      "Kumar",
      "2025-08-30",
      2874.92,
      772.82,
      "Overdue"
    ],
    [
      "Lata",
      "Joshi",
      "2025-08-29",
      986.51,
      177.23,
      "Overdue"
    ],
    [
      "Swati",
      "Mishra",
      "2025-08-26",
      2886.46,
      271.51,
      "Pending"
    ],
    [
      "Kunal",
      "Rao",
      "2025-08-24",
      6779.19,
      2083.08,
      "Pending"
    ],
    [
      "Deepak",
      "Iyer",
      "2025-08-21",
      3013.37,
      785.75,
      "Pending"
    ],
    [
      "Vijay",
      "Pandey",
      "2025-08-20",
      1773.18,
      33.76,
      "Overdue"
    ],
    [
      "Tanvi",
      "Malhotra",
      "2025-08-20",
      1269.22,
      228.25,
      "Pending"
    ],
    [
      "Ayaan",
      "Patel",
      "2025-08-16",
      609.34,
      148.53,
      "Overdue"
    ],
    [
      "Nikhil",
      "Nair",
      "2025-08-13",
      3634.06,
      1135.19,
      "Pending"
    ],
    [
      "Ayaan",
      "Kumar",
      "2025-08-13",
      7617.95,
      494.81,
      "Overdue"
    ],
    [
      "Swati",
      "Mishra",
      "2025-08-11",
      4840.37,
      639.59,
      "Pending"
    ],
    [
      "Isha",
      "Kumar",
      "2025-08-08",
      6963.21,
      431.92,
      "Overdue"
    ],
    [
      "Asha",
      "Iyer",
      "2025-08-05",
      6423.18,
      1829.04,
      "Pending"
    ],
    [
      "Tanvi",
      "Bose",
      "2025-07-30",
      4842.89,
      908.64,
      "Overdue"
    ],
    [
      "Rekha",
      "Kapoor",
      "2025-07-30",
      2661.12,
      189.22,
      "Pending"
    ],
    [
      "Divya",
      "Shah",
      "2025-07-27",
      2339.2,
      1123.69,
      "Pending"
    ],
    [
      "Rahul",
      "Joshi",
      "2025-07-26",
      1038.19,
      373.92,
      "Pending"
    ],
    [
      "Kunal",
      "Singh",
      "2025-07-26",
      7610.63,
      2238.15,
      "Overdue"
    ],
    [
      "Aditya",
      "Kapoor",
      "2025-07-21",
      1294.02,
      136.84,
      "Pending"
    ],
    [
      "Isha",
      "Mehta",
      "2025-07-21",
      401.86,
      19.18,
      "Pending"
    ],
    [
      "Ayaan",
      "Patel",
      "2025-07-16",
      4343.78,
      1353.44,
      "Pending"
    ],
    [
      "Harsh",
      "Rao",
      "2025-07-14",
      6279.46,
      1039.87,
      "Overdue"
    ],
    [
      "Preeti",
      "Shah",
      "2025-07-09",
      2216.18,
      410.22,
      "Pending"
    ],
    [
      "Tara",
      "Sharma",
      "2025-07-08",
      5879.8,
      2907.9,
      "Pending"
    ],
    [
      "Sanjay",
      "Malhotra",
      "2025-07-05",
      1093.79,
      262.71,
      "Overdue"
    ],
    [
      "Varun",
      "Shah",
      "2025-06-30",
      6516.9,
      643.94,
      "Overdue"
    ],
    [
      "Pankaj",
      "Shah",
      "2025-06-29",
      4009.96,
      1085.5,
      "Pending"
    ],
    [
      "Ayaan",
      "Chopra",
      "2025-06-27",
      3499.21,
      1481.27,
      "Pending"
    ],
    [
      "Asha",
      "Verma",
      "2025-06-22",
      6878.71,
      674.99,
      "Pending"
    ],
    [
      "Kavya",
      "Mehta",
      "2025-06-17",
      3640.94,
      475.06,
      "Overdue"
    ],
    [
      "Manish",
      "Malhotra",
      "2025-06-14",
      5806.13,
      1592.45,
      "Overdue"
    ],
    [
      "Tanvi",
      "Malhotra",
      "2025-06-14",
      4080.44,
      976.11,
      "Overdue"
    ],
    [
      "Asha",
      "Patel",
      "2025-06-14",
      4142.08,
      1259.85,
      "Pending"
    ],
    [
      "Suresh",
      "Sharma",
      "2025-06-13",
      768.98,
      230.51,
      "Pending"
    ],
    [
      "Ayaan",
      "Bose",
      "2025-06-12",
      3663.48,
      784.56,
      "Overdue"
    ],
    [
      "Kunal",
      "Reddy",
      "2025-06-10",
      7922.63,
      3197.6,
      "Pending"
    ],
    [
      "Abhishek",
      "Das",
      "2025-06-03",
      475.44,
      172.58,
      "Pending"
    ],
    [
      "Riya",
      "Rao",
      "2025-06-03",
      1694.97,
      460.96,
      "Overdue"
    ],
    [
      "Divya",
      "Das",
      "2025-06-02",
      6937.46,
      2922.38,
      "Pending"
    ],
    [
      "Siddharth",
      "Das",
      "2025-05-31",
      6145.53,
      951.62,
      "Overdue"
    ],
    [
      "Shreya",
      "Verma",
      "2025-05-25",
      1143.99,
      158.43,
      "Overdue"
    ],
    [
      "Suresh",
      "Kapoor",
      "2025-05-23",
      3223.52,
      160.85,
      "Pending"
    ],
    [
      "Ayaan",
      "Mehta",
      "2025-05-20",
      5536.88,
      245.91,
      "Overdue"
    ],
    [
      "Preeti",
      "Mehta",
      "2025-05-16",
      4772.83,
      1720.47,
      "Pending"
    ],
    [
      "Arjun",
      "Pandey",
      "2025-05-13",
      3269.68,
      955.17,
      "Overdue"
    ],
    [
      "Ananya",
      "Singh",
      "2025-05-10",
      6665.69,
      2262.82,
      "Pending"
    ],
    [
      "Varun",
      "Shah",
      "2025-05-08",
      5832.52,
      562.32,
      "Overdue"
    ],
    [
      "Nikhil",
      "Reddy",
      "2025-05-04",
      3202.66,
      574.31,
      "Overdue"
    ],
    [
      "Manish",
      "Shah",
      "2025-05-01",
      4182.07,
      1160.82,
      "Pending"
    ],
    [
      "Kunal",
      "Rao",
      "2025-04-29",
      4395.19,
      1868.66,
      "Pending"
    ],
    [
      "Ayaan",
      "Bose",
      "2025-04-28",
      6810.68,
      2215.18,
      "Pending"
    ],
    [
      "Tara",
      "Sharma",
      "2025-04-18",
      5413.2,
      1798.24,
      "Pending"
    ],
    [
      "Vijay",
      "Pandey",
      "2025-04-17",
      4082.99,
      809.21,
      "Pending"
    ],
    [
      "Suresh",
      "Mehta",
      "2025-04-16",
      7723.26,
      1804.8,
      "Pending"
    ],
    [
      "Tara",
      "Shah",
      "2025-04-16",
      2590.5,
      407.46,
      "Overdue"
    ],
    [
      "Suresh",
      "Kapoor",
      "2025-04-14",
      781.06,
      239.82,
      "Pending"
    ],
    [
      "Shreya",
      "Verma",
      "2025-04-08",
      6003.72,
      1970.66,
      "Pending"
    ],
    [
      "Tara",
      "Pandey",
      "2025-04-07",
      5659.29,
      20.41,
      "Overdue"
    ],
    [
      "Aditya",
      "Joshi",
      "2025-04-07",
      6112.96,
      888.3,
      "Pending"
    ]
  ],
  "row_count": 142,
  "chart": {
    "data": [
      {
        "name": "total_amount",
        "x": [
          "Kavya",
          "Amit",
          "Tanvi",
          "Kavya",
          "Harsh",
          "Suresh",
          "Meera",
          "Ananya",
          "Divya",
          "Yash",
          "Riya",
          "Asha",
          "Tara",
          "Asha",
          "Rajesh",
          "Pankaj",
          "Rajesh",
          "Riya",
          "Asha",
          "Manoj",
          "Rekha",
          "Abhishek",
          "Kavita",
          "Asha",
          "Manish",
          "Asha",
          "Tara",
          "Tara",
          "Rekha",
          "Vijay",
          "Amit",
          "Ananya",
          "Naina",
          "Siddharth",
          "Manoj",
          "Aarav",
          "Manish",
          "Varun",
          "Aditya",
          "Ankita",
          "Rekha",
          "Ayaan",
          "Lata",
          "Meera",
          "Suresh",
          "Ayaan",
          "Swati",
          "Rahul",
          "Rajesh",
          "Swati",
          "Sanjay",
          "Riya",
          "Riya",
          "Asha",
          "Pooja",
          "Isha",
          "Manoj",
          "Usha",
          "Siddharth",
          "Divya",
          "Pankaj",
          "Kavita",
          "Arjun",
          "Ankita",
          "Kunal",
          "Aditya",
          "Naina",
          "Kavita",
          "Harsh",
          "Vijay",
          "Riya",
          "Manish",
          "Shreya",
          "Ankita",
          "Amit",
          "Kavya",
          "Varun",
          "Vijay",
          "Ayaan",
          "Preeti",
          "Kunal",
          "Naina",
          "Kunal",
          "Pankaj",
          "Lata",
          "Swati",
          "Kunal",
          "Deepak",
          "Vijay",
          "Tanvi",
          "Ayaan",
          "Nikhil",
          "Ayaan",
          "Swati",
          "Isha",
          "Asha",
          "Tanvi",
          "Rekha",
          "Divya",
          "Rahul",
          "Kunal",
          "Aditya",
          "Isha",
          "Ayaan",
          "Harsh",
          "Preeti",
          "Tara",
          "Sanjay",
          "Varun",
          "Pankaj",
          "Ayaan",
          "Asha",
          "Kavya",
          "Manish",
          "Tanvi",
          "Asha",
          "Suresh",
          "Ayaan",
          "Kunal",
          "Abhishek",
          "Riya",
          "Divya",
          "Siddharth",
          "Shreya",
          "Suresh",
          "Ayaan",
          "Preeti",
          "Arjun",
          "Ananya",
          "Varun",
          "Nikhil",
          "Manish",
          "Kunal",
          "Ayaan",
          "Tara",
          "Vijay",
          "Suresh",
          "Tara",
          "Suresh",
          "Shreya",
          "Tara",
          "Aditya"
        ],
        "y": [
          461.47,
          606.39,
          4584.72,
          1625.88,
          4872.22,
          4640.06,
          2112.88,
          708.78,
          417.22,
          5913.55,
          1600.16,
          6337.03,
          6230.14,
          348.59,
          2792.2,
          1795.85,
          6373.16,
          822.4,
          2769.23,
          3200.69,
          3360.84,
          2955.07,
          6468.59,
          5862.7,
          1481.53,
          6984.07,
          5524.87,
          5202.75,
          1311.87,
          5485.59,
          828.17,
          6839.46,
          7142.16,
          5915.26,
          6481.89,
          2042.58,
          6014.27,
          1424.21,
          5434.43,
          6862.05,
          1843.79,
          1125.29,
          1543.23,
          750.47,
          7605.65,
          702.57,
          2926.44,
          6051.24,
          4877.21,
          418.92,
          6464.26,
          1427.85,
          6499.8,
          3749.65,
          1561.23,
          5492.56,
          1509.14,
          3663.52,
          4656.04,
          4244.75,
          6464.24,
          4217.27,
          3317.49,
          7745.02,
          703.55,
          7608.31,
          4060.96,
          418.7,
          4527.36,
          4514.4,
          1498.82,
          729.15,
          6693.75,
          5916.35,
          3520.36,
          5241.1,
          6362.39,
          657.06,
          4660.02,
          2675.64,
          5442.88,
          6373.45,
          3446.59,
          2874.92,
          986.51,
          2886.46,
          6779.19,
          3013.37,
          1773.18,
          1269.22,
          609.34,
          3634.06,
          7617.95,
          4840.37,
          6963.21,
          6423.18,
          4842.89,
          2661.12,
          2339.2,
          1038.19,
          7610.63,
          1294.02,
          401.86,
          4343.78,
          6279.46,
          2216.18,
          5879.8,
          1093.79,
          6516.9,
          4009.96,
          3499.21,
          6878.71,
          3640.94,
          5806.13,
          4080.44,
          4142.08,
          768.98,
          3663.48,
          7922.63,
          475.44,
          1694.97,
          6937.46,
          6145.53,
          1143.99,
          3223.52,
          5536.88,
          4772.83,
          3269.68,
          6665.69,
          5832.52,
          3202.66,
          4182.07,
          4395.19,
          6810.68,
          5413.2,
          4082.99,
          7723.26,
          2590.5,
          781.06,
          6003.72,
          5659.29,
          6112.96
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "total_amount by first_name"
      },
      "xaxis": {
        "title": {
          "text": "first_name"
        }
      },
      "yaxis": {
        "title": {
          "text": "total_amount"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

14) What percentage of appointments are no-shows?
{
  "message": "Here are the 1 results:",
  "sql_query": "SELECT ROUND( 100.0 * SUM(CASE WHEN status = 'No-Show' THEN 1 ELSE 0 END) / COUNT(*), 2 ) AS no_show_percentage FROM appointments",
  "columns": [
    "no_show_percentage"
  ],
  "rows": [
    [
      19.6
    ]
  ],
  "row_count": 1,
  "chart": null,
  "chart_type": null,
  "error": null
}

15) Show the busiest day of the week for appointments
{
  "message": "Here are the 1 results:",
  "sql_query": "SELECT CASE strftime('%w', appointment_date) WHEN '0' THEN 'Sunday' WHEN '1' THEN 'Monday' WHEN '2' THEN 'Tuesday' WHEN '3' THEN 'Wednesday' WHEN '4' THEN 'Thursday' WHEN '5' THEN 'Friday' WHEN '6' THEN 'Saturday' END AS weekday, COUNT(*) AS appointment_count FROM appointments GROUP BY weekday ORDER BY appointment_count DESC LIMIT 1",
  "columns": [
    "weekday",
    "appointment_count"
  ],
  "rows": [
    [
      "Monday",
      86
    ]
  ],
  "row_count": 1,
  "chart": {
    "data": [
      {
        "name": "appointment_count",
        "x": [
          "Monday"
        ],
        "y": [
          86
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "appointment_count by weekday"
      },
      "xaxis": {
        "title": {
          "text": "weekday"
        }
      },
      "yaxis": {
        "title": {
          "text": "appointment_count"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

16)Revenue trend by month
{
  "message": "Found 12 results.",
  "sql_query": "SELECT strftime('%Y-%m', invoice_date) AS month, SUM(total_amount) AS total_revenue FROM invoices GROUP BY month ORDER BY month",
  "columns": [
    "month",
    "total_revenue"
  ],
  "rows": [
    [
      "2025-04",
      90864.9
    ],
    [
      "2025-05",
      97348.26
    ],
    [
      "2025-06",
      132114.88
    ],
    [
      "2025-07",
      88329.66
    ],
    [
      "2025-08",
      124224.81999999999
    ],
    [
      "2025-09",
      105420.05
    ],
    [
      "2025-10",
      78950.65
    ],
    [
      "2025-11",
      107794.36
    ],
    [
      "2025-12",
      149238.28
    ],
    [
      "2026-01",
      85875.16
    ],
    [
      "2026-02",
      72329.82
    ],
    [
      "2026-03",
      60863.07
    ]
  ],
  "row_count": 12,
  "chart": {
    "data": [
      {
        "name": "total_revenue",
        "x": [
          "2025-04",
          "2025-05",
          "2025-06",
          "2025-07",
          "2025-08",
          "2025-09",
          "2025-10",
          "2025-11",
          "2025-12",
          "2026-01",
          "2026-02",
          "2026-03"
        ],
        "y": [
          90864.9,
          97348.26,
          132114.88,
          88329.66,
          124224.81999999999,
          105420.05,
          78950.65,
          107794.36,
          149238.28,
          85875.16,
          72329.82,
          60863.07
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "total_revenue by month"
      },
      "xaxis": {
        "title": {
          "text": "month"
        }
      },
      "yaxis": {
        "title": {
          "text": "total_revenue"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

17)Average appointment duration by doctor
{
  "message": "Found 15 results.",
  "sql_query": "SELECT d.name, ROUND(AVG(t.duration_minutes), 2) AS avg_duration FROM treatments t JOIN appointments a ON a.id = t.appointment_id JOIN doctors d ON d.id = a.doctor_id GROUP BY d.id, d.name ORDER BY avg_duration DESC",
  "columns": [
    "name",
    "avg_duration"
  ],
  "rows": [
    [
      "Dr. Reena Shah",
      88.1
    ],
    [
      "Dr. Ankit Malhotra",
      83.33
    ],
    [
      "Dr. Neha Gupta",
      79.2
    ],
    [
      "Dr. Arun Kapoor",
      78.58
    ],
    [
      "Dr. Kavita Reddy",
      76.36
    ],
    [
      "Dr. Manish Verma",
      71.25
    ],
    [
      "Dr. Sunita Pandey",
      68.07
    ],
    [
      "Dr. Priti Nair",
      67.45
    ],
    [
      "Dr. Rahul Bose",
      66.97
    ],
    [
      "Dr. Sameer Joshi",
      66.52
    ],
    [
      "Dr. Rajesh Sharma",
      65
    ],
    [
      "Dr. Meena Pillai",
      64.65
    ],
    [
      "Dr. Suresh Iyer",
      62
    ],
    [
      "Dr. Divya Singh",
      56.63
    ],
    [
      "Dr. Vijay Mehta",
      50.92
    ]
  ],
  "row_count": 15,
  "chart": {
    "data": [
      {
        "name": "avg_duration",
        "x": [
          "Dr. Reena Shah",
          "Dr. Ankit Malhotra",
          "Dr. Neha Gupta",
          "Dr. Arun Kapoor",
          "Dr. Kavita Reddy",
          "Dr. Manish Verma",
          "Dr. Sunita Pandey",
          "Dr. Priti Nair",
          "Dr. Rahul Bose",
          "Dr. Sameer Joshi",
          "Dr. Rajesh Sharma",
          "Dr. Meena Pillai",
          "Dr. Suresh Iyer",
          "Dr. Divya Singh",
          "Dr. Vijay Mehta"
        ],
        "y": [
          88.1,
          83.33,
          79.2,
          78.58,
          76.36,
          71.25,
          68.07,
          67.45,
          66.97,
          66.52,
          65,
          64.65,
          62,
          56.63,
          50.92
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "avg_duration by name"
      },
      "xaxis": {
        "title": {
          "text": "name"
        }
      },
      "yaxis": {
        "title": {
          "text": "avg_duration"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

18)List patients with overdue invoices
{
  "message": "Here are the 63 results:",
  "sql_query": "SELECT DISTINCT p.first_name, p.last_name, p.email, p.phone, i.total_amount, i.paid_amount, i.status FROM patients p JOIN invoices i ON i.patient_id = p.id WHERE i.status = 'Overdue' ORDER BY i.total_amount DESC",
  "columns": [
    "first_name",
    "last_name",
    "email",
    "phone",
    "total_amount",
    "paid_amount",
    "status"
  ],
  "rows": [
    [
      "Ankita",
      "Chopra",
      "ankita.chopra13@email.com",
      "919553670840",
      7745.02,
      849.31,
      "Overdue"
    ],
    [
      "Ayaan",
      "Kumar",
      "ayaan.kumar70@email.com",
      "916371249943",
      7617.95,
      494.81,
      "Overdue"
    ],
    [
      "Kunal",
      "Singh",
      "kunal.singh68@email.com",
      "917915573325",
      7610.63,
      2238.15,
      "Overdue"
    ],
    [
      "Aditya",
      "Chopra",
      null,
      null,
      7608.31,
      538.16,
      "Overdue"
    ],
    [
      "Naina",
      "Kapoor",
      null,
      null,
      7142.16,
      453.13,
      "Overdue"
    ],
    [
      "Isha",
      "Kumar",
      "isha.kumar88@email.com",
      "916083074505",
      6963.21,
      431.92,
      "Overdue"
    ],
    [
      "Ankita",
      "Nair",
      "ankita.nair27@email.com",
      "918658354878",
      6862.05,
      547.15,
      "Overdue"
    ],
    [
      "Ananya",
      "Mishra",
      "ananya.mishra75@email.com",
      "918755386726",
      6839.46,
      160.73,
      "Overdue"
    ],
    [
      "Shreya",
      "Verma",
      "shreya.verma81@email.com",
      "917111728003",
      6693.75,
      637.03,
      "Overdue"
    ],
    [
      "Varun",
      "Shah",
      "varun.shah37@email.com",
      "918581794231",
      6516.9,
      643.94,
      "Overdue"
    ],
    [
      "Riya",
      "Rao",
      "riya.rao77@email.com",
      "918598096576",
      6499.8,
      1166.12,
      "Overdue"
    ],
    [
      "Kavita",
      "Rao",
      "kavita.rao86@email.com",
      "916373736017",
      6468.59,
      1549.66,
      "Overdue"
    ],
    [
      "Sanjay",
      "Patel",
      "sanjay.patel76@email.com",
      "917386328373",
      6464.26,
      29.84,
      "Overdue"
    ],
    [
      "Naina",
      "Kapoor",
      null,
      null,
      6373.45,
      727.48,
      "Overdue"
    ],
    [
      "Asha",
      "Malhotra",
      "asha.malhotra13@email.com",
      "917819932320",
      6337.03,
      1113.35,
      "Overdue"
    ],
    [
      "Harsh",
      "Rao",
      "harsh.rao79@email.com",
      "919736911203",
      6279.46,
      1039.87,
      "Overdue"
    ],
    [
      "Tara",
      "Pandey",
      null,
      "916349114602",
      6230.14,
      176.74,
      "Overdue"
    ],
    [
      "Siddharth",
      "Das",
      "siddharth.das62@email.com",
      "918955629082",
      6145.53,
      951.62,
      "Overdue"
    ],
    [
      "Rahul",
      "Joshi",
      "rahul.joshi26@email.com",
      "917842537485",
      6051.24,
      1183.52,
      "Overdue"
    ],
    [
      "Ankita",
      "Chopra",
      "ankita.chopra13@email.com",
      "919553670840",
      5916.35,
      560.65,
      "Overdue"
    ],
    [
      "Siddharth",
      "Malhotra",
      "siddharth.malhotra20@email.com",
      "916537371314",
      5915.26,
      470.9,
      "Overdue"
    ],
    [
      "Asha",
      "Verma",
      "asha.verma9@email.com",
      "917759680902",
      5862.7,
      1689.75,
      "Overdue"
    ],
    [
      "Varun",
      "Shah",
      "varun.shah37@email.com",
      "918581794231",
      5832.52,
      562.32,
      "Overdue"
    ],
    [
      "Manish",
      "Malhotra",
      "manish.malhotra29@email.com",
      "917043391135",
      5806.13,
      1592.45,
      "Overdue"
    ],
    [
      "Tara",
      "Pandey",
      null,
      "916349114602",
      5659.29,
      20.41,
      "Overdue"
    ],
    [
      "Ayaan",
      "Mehta",
      null,
      "918135495357",
      5536.88,
      245.91,
      "Overdue"
    ],
    [
      "Tara",
      "Shah",
      "tara.shah46@email.com",
      "918245244551",
      5524.87,
      29.42,
      "Overdue"
    ],
    [
      "Isha",
      "Kumar",
      "isha.kumar88@email.com",
      "916083074505",
      5492.56,
      1157.92,
      "Overdue"
    ],
    [
      "Kunal",
      "Rao",
      "kunal.rao88@email.com",
      "918492626389",
      5442.88,
      52.23,
      "Overdue"
    ],
    [
      "Tara",
      "Shah",
      null,
      "917300200362",
      5202.75,
      470.38,
      "Overdue"
    ],
    [
      "Tanvi",
      "Bose",
      "tanvi.bose58@email.com",
      "919368292965",
      4842.89,
      908.64,
      "Overdue"
    ],
    [
      "Suresh",
      "Kapoor",
      "suresh.kapoor69@email.com",
      null,
      4640.06,
      756.67,
      "Overdue"
    ],
    [
      "Kavita",
      "Iyer",
      null,
      "918185065473",
      4217.27,
      878.03,
      "Overdue"
    ],
    [
      "Tanvi",
      "Malhotra",
      null,
      "916095554034",
      4080.44,
      976.11,
      "Overdue"
    ],
    [
      "Asha",
      "Verma",
      "asha.verma22@email.com",
      "917424346200",
      3749.65,
      641.57,
      "Overdue"
    ],
    [
      "Ayaan",
      "Bose",
      null,
      "918619765931",
      3663.48,
      784.56,
      "Overdue"
    ],
    [
      "Kavya",
      "Mehta",
      "kavya.mehta96@email.com",
      "919125472323",
      3640.94,
      475.06,
      "Overdue"
    ],
    [
      "Kunal",
      "Singh",
      "kunal.singh68@email.com",
      "917915573325",
      3446.59,
      743.9,
      "Overdue"
    ],
    [
      "Rekha",
      "Patel",
      "rekha.patel28@email.com",
      "919140079149",
      3360.84,
      200.96,
      "Overdue"
    ],
    [
      "Arjun",
      "Pandey",
      "arjun.pandey75@email.com",
      "918863364783",
      3269.68,
      955.17,
      "Overdue"
    ],
    [
      "Nikhil",
      "Reddy",
      "nikhil.reddy36@email.com",
      "919623614246",
      3202.66,
      574.31,
      "Overdue"
    ],
    [
      "Manoj",
      "Pandey",
      "manoj.pandey15@email.com",
      "919718000150",
      3200.69,
      588.55,
      "Overdue"
    ],
    [
      "Swati",
      "Kapoor",
      "swati.kapoor25@email.com",
      "918929551535",
      2926.44,
      786.37,
      "Overdue"
    ],
    [
      "Pankaj",
      "Kumar",
      "pankaj.kumar37@email.com",
      "917420565703",
      2874.92,
      772.82,
      "Overdue"
    ],
    [
      "Rajesh",
      "Kapoor",
      "rajesh.kapoor21@email.com",
      "917538485617",
      2792.2,
      38.21,
      "Overdue"
    ],
    [
      "Preeti",
      "Iyer",
      "preeti.iyer61@email.com",
      "916168784478",
      2675.64,
      550.01,
      "Overdue"
    ],
    [
      "Tara",
      "Shah",
      "tara.shah46@email.com",
      "918245244551",
      2590.5,
      407.46,
      "Overdue"
    ],
    [
      "Vijay",
      "Pandey",
      null,
      "919572859104",
      1773.18,
      33.76,
      "Overdue"
    ],
    [
      "Riya",
      "Rao",
      "riya.rao77@email.com",
      "918598096576",
      1694.97,
      460.96,
      "Overdue"
    ],
    [
      "Riya",
      "Nair",
      "riya.nair15@email.com",
      null,
      1600.16,
      29.92,
      "Overdue"
    ],
    [
      "Pooja",
      "Rao",
      "pooja.rao52@email.com",
      "916470317642",
      1561.23,
      99.78,
      "Overdue"
    ],
    [
      "Lata",
      "Malhotra",
      null,
      "918247629777",
      1543.23,
      267.75,
      "Overdue"
    ],
    [
      "Rekha",
      "Patel",
      "rekha.patel28@email.com",
      "919140079149",
      1311.87,
      214.16,
      "Overdue"
    ],
    [
      "Shreya",
      "Verma",
      "shreya.verma81@email.com",
      "917111728003",
      1143.99,
      158.43,
      "Overdue"
    ],
    [
      "Sanjay",
      "Malhotra",
      "sanjay.malhotra39@email.com",
      "918712413894",
      1093.79,
      262.71,
      "Overdue"
    ],
    [
      "Lata",
      "Joshi",
      "lata.joshi92@email.com",
      "917686965492",
      986.51,
      177.23,
      "Overdue"
    ],
    [
      "Riya",
      "Nair",
      "riya.nair15@email.com",
      null,
      822.4,
      24.66,
      "Overdue"
    ],
    [
      "Manish",
      "Malhotra",
      "manish.malhotra29@email.com",
      "917043391135",
      729.15,
      197.39,
      "Overdue"
    ],
    [
      "Ananya",
      "Mishra",
      "ananya.mishra75@email.com",
      "918755386726",
      708.78,
      138.04,
      "Overdue"
    ],
    [
      "Vijay",
      "Verma",
      "vijay.verma85@email.com",
      "917349198436",
      657.06,
      42.1,
      "Overdue"
    ],
    [
      "Ayaan",
      "Patel",
      "ayaan.patel83@email.com",
      "917039872155",
      609.34,
      148.53,
      "Overdue"
    ],
    [
      "Amit",
      "Shah",
      "amit.shah81@email.com",
      "919372790114",
      606.39,
      93.74,
      "Overdue"
    ],
    [
      "Kavita",
      "Mehta",
      "kavita.mehta26@email.com",
      null,
      418.7,
      110.38,
      "Overdue"
    ]
  ],
  "row_count": 63,
  "chart": {
    "data": [
      {
        "name": "phone",
        "x": [
          "Ankita",
          "Ayaan",
          "Kunal",
          "Aditya",
          "Naina",
          "Isha",
          "Ankita",
          "Ananya",
          "Shreya",
          "Varun",
          "Riya",
          "Kavita",
          "Sanjay",
          "Naina",
          "Asha",
          "Harsh",
          "Tara",
          "Siddharth",
          "Rahul",
          "Ankita",
          "Siddharth",
          "Asha",
          "Varun",
          "Manish",
          "Tara",
          "Ayaan",
          "Tara",
          "Isha",
          "Kunal",
          "Tara",
          "Tanvi",
          "Suresh",
          "Kavita",
          "Tanvi",
          "Asha",
          "Ayaan",
          "Kavya",
          "Kunal",
          "Rekha",
          "Arjun",
          "Nikhil",
          "Manoj",
          "Swati",
          "Pankaj",
          "Rajesh",
          "Preeti",
          "Tara",
          "Vijay",
          "Riya",
          "Riya",
          "Pooja",
          "Lata",
          "Rekha",
          "Shreya",
          "Sanjay",
          "Lata",
          "Riya",
          "Manish",
          "Ananya",
          "Vijay",
          "Ayaan",
          "Amit",
          "Kavita"
        ],
        "y": [
          "919553670840",
          "916371249943",
          "917915573325",
          null,
          null,
          "916083074505",
          "918658354878",
          "918755386726",
          "917111728003",
          "918581794231",
          "918598096576",
          "916373736017",
          "917386328373",
          null,
          "917819932320",
          "919736911203",
          "916349114602",
          "918955629082",
          "917842537485",
          "919553670840",
          "916537371314",
          "917759680902",
          "918581794231",
          "917043391135",
          "916349114602",
          "918135495357",
          "918245244551",
          "916083074505",
          "918492626389",
          "917300200362",
          "919368292965",
          null,
          "918185065473",
          "916095554034",
          "917424346200",
          "918619765931",
          "919125472323",
          "917915573325",
          "919140079149",
          "918863364783",
          "919623614246",
          "919718000150",
          "918929551535",
          "917420565703",
          "917538485617",
          "916168784478",
          "918245244551",
          "919572859104",
          "918598096576",
          null,
          "916470317642",
          "918247629777",
          "919140079149",
          "917111728003",
          "918712413894",
          "917686965492",
          null,
          "917043391135",
          "918755386726",
          "917349198436",
          "917039872155",
          "919372790114",
          null
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "phone by first_name"
      },
      "xaxis": {
        "title": {
          "text": "first_name"
        }
      },
      "yaxis": {
        "title": {
          "text": "phone"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

19)Compare revenue between departments
{
  "message": "Found 5 results.",
  "sql_query": "SELECT d.department, SUM(i.total_amount) AS total_revenue FROM invoices i JOIN appointments a ON a.patient_id = i.patient_id JOIN doctors d ON d.id = a.doctor_id GROUP BY d.department ORDER BY total_revenue DESC",
  "columns": [
    "department",
    "total_revenue"
  ],
  "rows": [
    [
      "Bone & Joint",
      833234.25
    ],
    [
      "Skin Care",
      716003.35
    ],
    [
      "General Medicine",
      484762.98
    ],
    [
      "Heart & Vascular",
      472556.3
    ],
    [
      "Child Health",
      341220.66
    ]
  ],
  "row_count": 5,
  "chart": {
    "data": [
      {
        "name": "total_revenue",
        "x": [
          "Bone & Joint",
          "Skin Care",
          "General Medicine",
          "Heart & Vascular",
          "Child Health"
        ],
        "y": [
          833234.25,
          716003.35,
          484762.98,
          472556.3,
          341220.66
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "total_revenue by department"
      },
      "xaxis": {
        "title": {
          "text": "department"
        }
      },
      "yaxis": {
        "title": {
          "text": "total_revenue"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}

20)Show patient registration trend by month
{
  "message": "Here are the 36 results:",
  "sql_query": "SELECT strftime('%Y-%m', registered_date) AS month, COUNT(*) AS new_patients FROM patients GROUP BY month ORDER BY month",
  "columns": [
    "month",
    "new_patients"
  ],
  "rows": [
    [
      "2023-04",
      1
    ],
    [
      "2023-05",
      4
    ],
    [
      "2023-06",
      3
    ],
    [
      "2023-07",
      4
    ],
    [
      "2023-08",
      7
    ],
    [
      "2023-09",
      8
    ],
    [
      "2023-10",
      3
    ],
    [
      "2023-11",
      2
    ],
    [
      "2023-12",
      7
    ],
    [
      "2024-01",
      4
    ],
    [
      "2024-02",
      3
    ],
    [
      "2024-03",
      7
    ],
    [
      "2024-04",
      6
    ],
    [
      "2024-05",
      5
    ],
    [
      "2024-06",
      8
    ],
    [
      "2024-07",
      4
    ],
    [
      "2024-08",
      8
    ],
    [
      "2024-09",
      4
    ],
    [
      "2024-10",
      8
    ],
    [
      "2024-11",
      9
    ],
    [
      "2024-12",
      6
    ],
    [
      "2025-01",
      10
    ],
    [
      "2025-02",
      9
    ],
    [
      "2025-03",
      6
    ],
    [
      "2025-04",
      5
    ],
    [
      "2025-05",
      4
    ],
    [
      "2025-06",
      8
    ],
    [
      "2025-07",
      4
    ],
    [
      "2025-08",
      6
    ],
    [
      "2025-09",
      5
    ],
    [
      "2025-10",
      4
    ],
    [
      "2025-11",
      6
    ],
    [
      "2025-12",
      5
    ],
    [
      "2026-01",
      9
    ],
    [
      "2026-02",
      2
    ],
    [
      "2026-03",
      6
    ]
  ],
  "row_count": 36,
  "chart": {
    "data": [
      {
        "name": "new_patients",
        "x": [
          "2023-04",
          "2023-05",
          "2023-06",
          "2023-07",
          "2023-08",
          "2023-09",
          "2023-10",
          "2023-11",
          "2023-12",
          "2024-01",
          "2024-02",
          "2024-03",
          "2024-04",
          "2024-05",
          "2024-06",
          "2024-07",
          "2024-08",
          "2024-09",
          "2024-10",
          "2024-11",
          "2024-12",
          "2025-01",
          "2025-02",
          "2025-03",
          "2025-04",
          "2025-05",
          "2025-06",
          "2025-07",
          "2025-08",
          "2025-09",
          "2025-10",
          "2025-11",
          "2025-12",
          "2026-01",
          "2026-02",
          "2026-03"
        ],
        "y": [
          1,
          4,
          3,
          4,
          7,
          8,
          3,
          2,
          7,
          4,
          3,
          7,
          6,
          5,
          8,
          4,
          8,
          4,
          8,
          9,
          6,
          10,
          9,
          6,
          5,
          4,
          8,
          4,
          6,
          5,
          4,
          6,
          5,
          9,
          2,
          6
        ],
        "type": "bar"
      }
    ],
    "layout": {
      "title": {
        "text": "new_patients by month"
      },
      "xaxis": {
        "title": {
          "text": "month"
        }
      },
      "yaxis": {
        "title": {
          "text": "new_patients"
        }
      },
      "showlegend": false
    }
  },
  "chart_type": "bar",
  "error": null
}