from injector import inject
from http.client import BAD_REQUEST
from flask_restful import abort
from injector import inject
from ulid import ULID

from api.domainlayer.password.IpasswordRepository import IpasswordRepository
from api.domainlayer.password.password import Password
from api.domainlayer.user.Iuserrepository import IuserRepository
from api.domainlayer.user.service.validateuser import ValidateUser
from api.domainlayer.user.user import User
from api.domainlayer.user.valueobject.email import Email

class CreateUser():
    """ユーザ作成ユースケース
    """    
    @inject
    def __init__(self, userrepository: IuserRepository, passwordrepository: IpasswordRepository, validateuser: ValidateUser):
        """インスタンス初期化

        Args:
            userrepository (IuserRepository): 
            passwordrepository (IpasswordRepository): [description]
            userservice (UserService): [description]
        """        
        self.userrepository: IuserRepository = userrepository
        self.passwordrepository: IpasswordRepository = passwordrepository
        self.validateuser: ValidateUser = validateuser
    
    def register(self, param: dict) -> None:
        """ユーザ作成処理

        Args:
            param (dict): ユーザの入力値(バリデーションはプレゼンテーション層)
        """        
        # ユーザ作成
        id: str  = str(ULID())
        email: Email = Email(param["email"])
        
        user: User = User(id, email)
        password: Password = Password(user.id, param["password"])
        
        self.validateuser.validate(user)
        
        # トランザクション処理にします
        self.userrepository.add(user)
        self.passwordrepository.add(password)
        

        