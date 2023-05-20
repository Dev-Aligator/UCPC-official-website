from django.core.validators import RegexValidator

class Validator:
    TeamRegex = RegexValidator(r'^[a-zA-Z0-9\u00C0-\u1EF9.]+$')
    NameRegex = RegexValidator(r'^[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\s\W|_]+$')
    NumberRegex = RegexValidator(r'^([0-9]{10}|[0-9]{11})$')
    AgeRegex = RegexValidator(r'^(1[6-9]|2[0-3])$')
    CMND_CCCDRegex = RegexValidator(r'^([0-9]{9}|[0-9]{12})$')
    MSSVRegex = RegexValidator(r'^[a-zA-Z0-9]+$')
    PhoneRegex = RegexValidator(r'(84|0[3|5|7|8|9])+([0-9]{8})\b')
    PwdRegex = RegexValidator(r'^(?=.{6,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)[ -~]*$')
    YearRegex = RegexValidator(r'^\d{4}$')
    JobTitleRegex = RegexValidator(r'^[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\s\W|_]+$')