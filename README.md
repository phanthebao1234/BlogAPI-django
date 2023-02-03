* AllowAny78 - bất kỳ người dùng nào, được xác thực hay không, đều có toàn quyền truy cập
* IsAuthenticated79 - chỉ những người dùng đã đăng ký, được xác thực mới có quyền truy cập
* IsAdminUser80 - chỉ quản trị viên/siêu người dùng mới có quyền truy cập
* IsAuthenticatedOrReadOnly81 - người dùng trái phép có thể xem bất kỳ trang nào nhưng chỉ những người dùng được xác thực mới có đặc quyền viết, chỉnh sửa hoặc xóa

***
## 4 KIỂU XÁC THỰC MÀ DJANGO REST FRAMEWORK HỖ TRỢ
1. **Basic Authentication** [Basic Authen](https://www.rfc-editor.org/rfc/rfc7617)
- Hình thức xác thực HTTP phổ biến nhất được gọi là Xác thực “Cơ bản”85. Khi một
khách hàng thực hiện một yêu cầu HTTP, nó buộc phải gửi thông tin xác thực đã được phê duyệt trước
quyền truy cập được cấp.
##### Mô hình
* Client makes an HTTP request
* Server responds with an HTTP response containing a 401 (Unauthorized) status code and
WWW-Authenticate HTTP header with details on how to authorize
* Client sends credentials back via the Authorization86 HTTP header
* Server checks credentials and responds with either 200 OK or 403 Forbidden status code
![Diagram](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication/http-auth-sequence-diagram.png)

**Ưu điểm:**
- Đơn giản
**Nhược điểm**:
- Đầu tiên, trên mỗi yêu cầu, máy chủ phải tra cứu và xác minh tên người dùng và mật khẩu, đó là không hiệu quả. Sẽ tốt hơn nếu tra cứu một lần và sau đó chuyển mã thông báo của một số loại cho biết, người dùng này được phê duyệt.
- Thứ hai, thông tin đăng nhập của người dùng đang được chuyển ở dạng văn bản rõ ràng, không phải được mã hóa hoàn toàn qua internet. Điều này là vô cùng không an toàn. Bất kỳ lưu lượng truy cập internet nào không được mã hóa đều có thể dễ dàng bị bắt và sử dụng lại. Do đó xác thực cơ bản chỉ nên được sử dụng thông qua HTTPS, phiên bản bảo mật của HTTP.

2. **Session Authentication**
- Các trang web nguyên khối, như Django truyền thống, từ lâu đã sử dụng một sơ đồ xác thực thay thế
đó là sự kết hợp giữa phiên và cookie. Ở mức cao, máy khách xác thực với
thông tin đăng nhập (tên người dùng/mật khẩu) và sau đó nhận ID phiên từ máy chủ được lưu trữ
như một chiếc bánh quy. ID phiên này sau đó được chuyển vào tiêu đề của mọi yêu cầu HTTP trong tương lai.
- Khi ID phiên được chuyển, máy chủ sẽ sử dụng nó để tra cứu đối tượng phiên chứa tất cả
thông tin cho một người dùng nhất định, bao gồm cả thông tin xác thực.
- Cách tiếp cận này mang tính trạng thái vì bản ghi phải được lưu giữ và duy trì trên cả máy chủ (the session object) và máy khách (the session ID).
##### Hãy xem lại quy trình cơ bản:
* Người dùng nhập thông tin đăng nhập của họ (thường là tên người dùng/mật khẩu)
* Máy chủ xác minh thông tin đăng nhập là chính xác và tạo một đối tượng phiên mà sau đó
được lưu trữ trong cơ sở dữ liệu
* Máy chủ gửi cho máy khách ID phiên—không phải bản thân đối tượng phiên—được lưu dưới dạng
cookie trên trình duyệt
* Đối với tất cả các yêu cầu trong tương lai, ID phiên được bao gồm dưới dạng tiêu đề HTTP và nếu được xác minh bởi
cơ sở dữ liệu, yêu cầu tiến hành
* Sau khi người dùng đăng xuất khỏi ứng dụng, ID phiên sẽ bị hủy bởi cả máy khách và
người phục vụ
* Nếu người dùng đăng nhập lại sau đó, ID phiên mới sẽ được tạo và lưu trữ dưới dạng cookie trên
khách hàng

##### Ưu điểm của phương pháp này là nó an toàn hơn vì thông tin đăng nhập của người dùng chỉ được gửi một lần chứ không phải trên mọi chu kỳ yêu cầu/phản hồi như trong Xác thực cơ bản. Nó cũng hiệu quả hơn vì máy chủ không phải xác minh thông tin đăng nhập của người dùng mỗi lần, nó chỉ khớp ID phiên với đối tượng phiên được tra cứu nhanh.
##### Tuy nhiên, có một số nhược điểm. Đầu tiên, ID phiên chỉ hợp lệ trong trình duyệt nơi đăng nhập đã được thực hiện; nó sẽ không hoạt động trên nhiều miền. Đây là một vấn đề hiển nhiên khi một API cần hỗ trợ nhiều giao diện người dùng như trang web và ứng dụng dành cho thiết bị di động. Thứ hai, các đối tượng phiên phải được cập nhật, điều này có thể gây khó khăn trong các trang web lớn có nhiều máy chủ. Làm thế nào để bạn duy trì tính chính xác của một đối tượng phiên trên mỗi máy chủ? Và thứ ba, các cookie được gửi đi cho mọi yêu cầu, ngay cả những yêu cầu không yêu cầu xác thực, điều này là không hiệu quả.
- => Do đó, thông thường không nên sử dụng sơ đồ xác thực dựa trên phiên cho bất kỳ API nào
sẽ có nhiều giao diện người dùng.

![Diagram](https://images.viblo.asia/full/e428d454-c208-451a-9586-69c9d68cc308.png)

3. **Token Authentication**
-