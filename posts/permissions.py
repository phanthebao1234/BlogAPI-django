from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Chỉ người dùng xác thực mới có quyền đọc
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Quyền đọc được cho phép với tất cả mọi người 
        # Cho phép các request như GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Quyền ghi chỉ cho phép tác giả của bài viết 
        return obj.author == request.user