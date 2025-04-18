# import UserClient từ model
from .models import UserClient, UserRating, Feedback
# import thư viện forms từ django
from django import  forms
from django.core.exceptions import ValidationError
# Tạo một đối tượng Form đăng ký kế thừa từ modelForm
class RegisterForm(forms.ModelForm):
    # Tạo hai biến password và rpassword = hai form dạng nhập là password với dạng text 
   
    rpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'rpassword', 'id': 'rpassword', 'onkeyup': 'batloirpassword()'}))
    
    # một class Meta dùng để thao tác với table trong database thông qua models
    class Meta: 
        model = UserClient
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',  'id': 'username', 'onkeyup': 'batloiusername()'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'id': 'email', 'onkeyup': 'batloiemail()'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'firstname', 'id': 'firstname', 'onkeyup': 'batloifirstname()'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'lastname', 'id': 'lastname', 'onkeyup': 'batloilastname()'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'name': 'phonenumber', 'id': 'phonenumber', 'onkeyup': 'batloiphonenumber()'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'id': 'password', 'onkeyup': 'batloipassword()'}),

        }    
        
        
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'passwordcu', 'onkeyup': 'return batloipasswordcu()'}), label="Mật khẩu cũ")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'passwordmoi', 'onkeyup': 'return batloipasswordmoi()'}), label="Mật khẩu mới")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'passwordr','onkeyup': 'return batloipasswordr()'}), label="Xác nhận mật khẩu mới")

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise ValidationError("Mật khẩu mới và xác nhận mật khẩu không khớp.")
        
        
        
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Nhập email mà bạn đã đăng ký', 'id': 'email', 'onkeyup': 'return batloiemail()'})
    )
    
    
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserClient
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class UserRatingForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 Sao'),
        (2, '2 Sao'),
        (3, '3 Sao'),
        (4, '4 Sao'),
        (5, '5 Sao'),
    ]
    
    rating = forms.ChoiceField(
        choices=RATING_CHOICES, 
        widget=forms.RadioSelect, 
        required=True
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Nhập đánh giá của bạn (tùy chọn)', 'class': 'form-control'}), 
        required=False
    )

    class Meta:
        model = UserRating
        fields = ['rating', 'comment']
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Nhập phản hồi của bạn...'
            })
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.order = kwargs.pop('order', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        feedback = super().save(commit=False)
        feedback.user = self.user
        feedback.order = self.order
        if commit:
            feedback.save()
        return feedback