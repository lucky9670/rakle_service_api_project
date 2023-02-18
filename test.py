results = [
    {
      "id": 1,
      "service": {
        "id": 1,
        "created_at": "2023-02-10T00:03:43.474340+05:30",
        "modified_at": "2023-02-10T00:03:43.474340+05:30",
        "transfer_date": "2023-02-10T00:03:43.474340+05:30",
        "ref": "2dcdfc58-7405-4f95-b38e-f11915d669a3",
        "service_name": "Test Services",
        "status": False,
        "service_image": "http://127.0.0.1:8000/media/service/image4-removebg-preview_f3X8O6q.png",
        "service_charge": "2000",
        "service_time": "5 day",
        "discount": "10",
        "main_cat_name": 1,
        "cat_name": 1,
        "main_service_name": 1
      },
      "created_at": "2023-02-10T00:52:16.811415+05:30",
      "modified_at": "2023-02-12T16:39:53.238936+05:30",
      "transfer_date": "2023-02-10T00:52:16.811415+05:30",
      "ref": "7dc9ad63-d8e0-461a-94c3-5590e2e6b457",
      "service_quantity": "1",
      "status": True,
      "user": 1,
      "user_device_id": None
    },
    {
      "id": 2,
      "service": {
        "id": 1,
        "created_at": "2023-02-10T00:03:43.474340+05:30",
        "modified_at": "2023-02-10T00:03:43.474340+05:30",
        "transfer_date": "2023-02-10T00:03:43.474340+05:30",
        "ref": "2dcdfc58-7405-4f95-b38e-f11915d669a3",
        "service_name": "Test Services",
        "status": False,
        "service_image": "http://127.0.0.1:8000/media/service/image4-removebg-preview_f3X8O6q.png",
        "service_charge": "2000",
        "service_time": "5 day",
        "discount": "10",
        "main_cat_name": 1,
        "cat_name": 1,
        "main_service_name": 1
      },
      "created_at": "2023-02-10T00:52:16.811415+05:30",
      "modified_at": "2023-02-12T16:39:53.238936+05:30",
      "transfer_date": "2023-02-10T00:52:16.811415+05:30",
      "ref": "7dc9ad63-d8e0-461a-94c3-5590e2e6b457",
      "service_quantity": "1",
      "status": True,
      "user": 1,
      "user_device_id": None
    },
    {
      "id": 1,
      "service": {
        "id": 1,
        "created_at": "2023-02-10T00:03:43.474340+05:30",
        "modified_at": "2023-02-10T00:03:43.474340+05:30",
        "transfer_date": "2023-02-10T00:03:43.474340+05:30",
        "ref": "2dcdfc58-7405-4f95-b38e-f11915d669a3",
        "service_name": "Test Services",
        "status": False,
        "service_image": "http://127.0.0.1:8000/media/service/image4-removebg-preview_f3X8O6q.png",
        "service_charge": "2000",
        "service_time": "5 day",
        "discount": "10",
        "main_cat_name": 1,
        "cat_name": 1,
        "main_service_name": 1
      },
      "created_at": "2023-02-10T00:52:16.811415+05:30",
      "modified_at": "2023-02-12T16:39:53.238936+05:30",
      "transfer_date": "2023-02-10T00:52:16.811415+05:30",
      "ref": "7dc9ad63-d8e0-461a-94c3-5590e2e6b457",
      "service_quantity": "1",
      "status": True,
      "user": 1,
      "user_device_id": None
    }
  ]
custom = []
for result in results:
    data = {
        "cart_id": result['id'],
        "service_id": result['service']["id"],
        "service_name": result['service']["service_name"],
    }
    custom.append(data)

print(custom)