# Tiểu luận chuyên ngành KTDL

Đề tài: Tìm hiểu https://superset.apache.org/ và xây dựng chương trình giống Power BI (Hệ đại trà)

GVHD: TS. Huỳnh Xuân Phụng

Thành viên nhóm:

Nguyễn Thành Công 18133004

Trịnh Công Viễn 18133061

#Hướng dẫn cài đặt sử dụng docker compose:

1.Tạo một mạng mới với tên là hadoop-network:

$ docker network create -d bridge my-bridge-network

Ví dụ: ($ docker network create --driver bridge hadoop-network --subnet=172.12.0.0/16)

2.Di chuyển vào thử mục postgresql và khởi chạy PostgreSQL:

$ docker-compose up -d

(Sử dụng PgAdmin để dễ dàng quản lý cơ sở dữ liệu hơn với địa chỉ http://0.0.0.0:5050 với User là admin, Password là 123)

3.Di chuyển vào thư mục superset và khởi chạy Superset:

$ docker-compose up -d

Truy cập vào Superset với địa chỉ http://127.0.0.1:8088

4.Để dừng sử dụng :

$ docker-compose down

5.Để lưu lại những kết quả thực hiện:

$ docker commit ID_Container
