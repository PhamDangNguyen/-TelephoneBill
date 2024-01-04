# Bài toán tính tiền điện thoại

## Tổng quan

Bài toán xây dựng chương trình tính tiền một người dùng (user) phải trả. Cách tính tiền cước như sau:

- Mỗi cuộc gọi được chia thành các block 30s. Số giây lẻ được tính thành 1 block. Ví dụ: cuộc gọi 6s được tính là 1 block. Cuộc gọi 36s được tính là 2 block.

- Số tiền cước mà người dùng phải trả là tổng số block họ đã gọi. Chương trình không cần chia theo tháng, năm, mà chỉ cần đưa ra số tổng.

## Ý tưởng thuật toán

#### API ghi nhận cuộc gọi

- Nếu là người dùng mới thì tên người dùng sẽ được lưu lại trong Dictionary như một mảng và thời gian cuộc gọi sẽ được đưa vào mảng tên người đó.

- Nếu là người dùng cũ, thời gian sẽ được đưa vào mảng chứa đại diện cho người dùng (có thể cộng dồn VD: Gọi 1 cuộc 10s, sau đó lại gọi 30s => mảng sẽ chứa 2 phần tử là 10s và 30s).

#### API hóa đơn Billing

Có thể nhập body cho API này nhưng để phù hợp bài toán em đã để đây là một quá trình tự động như sau:

- Nếu người dùng không có tên trong danh sách thu tiền => hóa đơn sẽ không được tạo.

- Nếu người dùng có tên trong danh sách thu tiền, thuật toán sẽ tiến hành:

1. Tính tổng thời gian đã gọi điện của người dùng.
2. Tính số block mà người dùng đã gọi.

## Phương pháp và công nghệ sử dụng

- API
- Python

## Requirement:

- fastapi==0.108.0
- pydantic==2.5.3
- uvicorn==0.25.0

## Hướng dẫn test code

- Cài đặt các thưu viện trong file requirement.txt.

- Chạy file main.py, trong cmd gõ lệnh "uvicorn main:app --reload" để thực hiện chương trình.
- Để test API có thể sử dụng phần mềm postman với API put sẽ truyền thời gian gọi mỗi cuộc điện thoại và tên người dùng theo đường dẫn, API get sẽ tính toán ra tổng số block mà người dùng đã thực hiện được.

## Demo video
https://github.com/PhamDangNguyen/TelephoneBill/assets/86046279/f579047d-66eb-40de-8dbf-1ddfc4b3b618
