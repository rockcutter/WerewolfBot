PHASE_RECEPTION = 0b00000000
PHASE_INPROGRESS = 0b10000000

class game(object):
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

        member = []
        status = PHASE_RECEPTION
        return 


    def Start(self):
        """
        statusをPHASE_INPROGRESSに変更する ゲームをスタートさせる

        Returns: 
            既にPHASE_INPROGRESSならFalse 機能通りに働いたならTrueを返す
        """
        if(status & PHASE_INPROGRESS == PHASE_INPROGRESS):
            return False
        status = PHASE_INPROGRESS
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

    def AddMember(self,name):
        """
        メンバーを追加する関数
        Args:
            string PlayerName
        """


        self.member.append(name)
        return

    