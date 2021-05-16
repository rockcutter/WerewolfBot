PHASE_RECEPTION = 0b00000000
PHASE_INPROGRESS = 0b10000000

class game():
    """ゲーム管理関連のクラス"""
    member = []
    status = PHASE_RECEPTION
    

    def __init__(self):
        """
        コンストラクタ 初期化メソッドを呼び出す
        """

        self.InitGame()
        return

    def InitGame(self):
        """
        初期化メソッド メンバ変数を初期化する際に呼び出される
        """

        self.member = []
        self.status = PHASE_RECEPTION
        return 

    def Start(self):
        """
        statusをPHASE_INPROGRESSに変更する ゲームをスタートさせる

        Returns: 
            既にPHASE_INPROGRESSならFalse 機能通りに働いたならTrueを返す
        """
        if(self.status & PHASE_INPROGRESS == PHASE_INPROGRESS):
            return False
        self.status = PHASE_INPROGRESS
        return True

    def Stop(self):
        """
        statusをPHASE_RECEPTIONに変更する ゲームをストップさせる

        Returns: 
            既にPHASE_RECEPTIONならFlase 機能通りに働いたならTrueを返す
        """
        if(status & PHASE_RECEPTION == PHASE_RECEPTION):
            return False
        status = PHASE_RECEPTION
        self.InitGame()
        return True

    def AddMember(self,playerData):
        """
        メンバーを追加する関数 同メンバーが入ることはない
        Args:
            string PlayerData :playerクラスのインスタンスを入れる
        Returns: 
            追加成功でTrue 失敗でFlase
        """
        for memberName in self.member:
            if(memberName.playerData == playerData.playerData):
                return False
        self.member.append(playerData)
        return True
    
    def GetMemberList(self):
        """
        メンバーリストを取得する関数
        Returns:
            メンバー情報が格納されたリスト
        """
        return self.member

    def GameInProgress(self):
        """
        ゲームが進行中か否かを返す
        Returns:
            ゲームが進行中ならTrue 逆はFalse
        """
        if(self.status & PHASE_INPROGRESS == PHASE_INPROGRESS):
            return True
        return False
        
    