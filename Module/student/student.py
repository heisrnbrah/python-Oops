class studentclass:
    def __init__(self):
        self.full_name = None
        self.date_of_birth = None
        self.age = None
        self.gender = None
        self.mobile_number = None
        self.email_address = None
        self.password = None
        self.preferred_language = None
        self.school_college_name = None
        self.class_grade = None
        self.board_curriculum = None
        self.academic_year = None
        self.tuition_subjects = []
        self.subject_levels = {}
        self.topics_needing_help = []
        self.parent_guardian_name = None
        self.parent_guardian_relationship = None
        self.parent_guardian_mobile_number = None
        self.parent_guardian_email_address = None
        self.preferred_communication_method = None

    def set_username_and_password(self, email, password):
        self.email_address = email
        self.password = password

    def setUsernameAndPassword(self, email, password):
        self.set_username_and_password(email, password)

    def set_usernameAndpassword(self, email, password):
        self.set_username_and_password(email, password)


StudentClass = studentclass