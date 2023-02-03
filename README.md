* AllowAny78 - bất kỳ người dùng nào, được xác thực hay không, đều có toàn quyền truy cập
* IsAuthenticated79 - chỉ những người dùng đã đăng ký, được xác thực mới có quyền truy cập
* IsAdminUser80 - chỉ quản trị viên/siêu người dùng mới có quyền truy cập
* IsAuthenticatedOrReadOnly81 - người dùng trái phép có thể xem bất kỳ trang nào nhưng chỉ những người dùng được xác thực mới có đặc quyền viết, chỉnh sửa hoặc xóa

## 4 KIỂU XÁC THỰC MÀ DJANGO REST FRAMEWORK HỖ TRỢ
* Basic Authentication
1. Client makes an HTTP request
2. Server responds with an HTTP response containing a 401 (Unauthorized) status code and
WWW-Authenticate HTTP header with details on how to authorize
3. Client sends credentials back via the Authorization86 HTTP header
4. Server checks credentials and responds with either 200 OK or 403 Forbidden status code