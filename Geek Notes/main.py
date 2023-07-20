from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import webbrowser
from kivy.core.window import Window

Window.size = (360,800)

screen_helper = """
ScreenManager:
    MenuScreen:
    ExamScreen:
    QueScreen:
    VideoScreen:
    ShareScreen:
    NotesScreen:
    Notes1Screen:
    CSScreen:
    CS3Screen:
    CS4Screen:
    CS5Screen:
    CS6Screen:
    CS7Screen:
    CS8Screen:
    DSScreen:
    ADEScreen:
    COScreen:
    SEScreen:
    DMSScreen:
    DAAScreen:
    OSScreen:
    MESScreen:
    OOPScreen:
    DCScreen:
    MEIScreen:
    CNSScreen:
    DBMSScreen:
    ATCScreen:
    ADPScreen:
    UNIXScreen:
    SSCScreen:
    CGVScreen:
    SMSScreen:
    WTAScreen:
    CCScreen:
    AJScreen:
    DMWScreen:
    SCMScreen:
    AIMLScreen:
    BDScreen:
    IOTScreen:
    SQLScreen:
    SANScreen:
    CS4VScreen:
    CS5VScreen:
    CS6VScreen:
    CS7VScreen:
    CS8VScreen:
    ECScreen:
    EC3Screen:
    EC4Screen:
    EC5Screen:
    EC6Screen:
    EC7Screen:
    EC8Screen:
    NTScreen:
    EDScreen:
    DSDScreen:
    COAScreen:
    PSIScreen:
    ACScreen:
    CSEScreen:
    ESLMScreen:
    SSScreen:
    MCScreen:
    MathScreen:
    TIMEScreen:
    DSPScreen:
    PACScreen:
    ITCScreen:
    WCScreen:
    VHDLScreen:
    DCEScreen:
    ESEScreen:
    MAAScreen:
    DSUVScreen:
    OSEScreen:
    PAPEScreen:
    ANNEScreen:
    JAVAEScreen:
    CNEScreen:
    CEScreen:
    RTSEScreen:
    SCEScreen:
    VLSIEScreen:
    WCCEScreen:
    OCNEScreen:
    NSEScreen:
    MEMSEScreen:
    PEAIEScreen:
    M1Screen:
    M2Screen:
    M3Screen:
    M4Screen:
    OptScreen:
    ExamttScreen:
    QuemainScreen:
    TtmathScreen:
    TtchemScreen:
    TtphyScreen:
    TtecScreen:
    TtmechScreen:
    TtcivilScreen:
    TtaimlScreen:
    QuemathScreen:
    QuechemScreen:
    QuephyScreen:
    QueecScreen:
    QuemechScreen:
    QuecivilScreen:
    QueaimlScreen:
<MenuScreen>:
    name: 'menu'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes' 
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'opt'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "DOODLE 720 1446 .png"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
    MDRectangleFlatButton:
        text: 'EXAM TIME TABLE'
        theme_text_color: "Custom" 
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "25sp"
        pos_hint: {'center_x':0.5,'center_y':0.66}
        size_hint: 0.82,0.182
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'examtt'
    Image:
        source: "EXAM Time Table.png"
        size_hint: 0.86,0.86
        pos_hint: {'center_x' :0.5, 'center_y' :0.66}
    MDRectangleFlatButton:
        text: 'QUESTION PAPER'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "25sp"
        pos_hint: {'center_x':0.5,'center_y':0.43}
        size_hint: 0.82,0.185
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'quemain'
    Image:
        source: "QPS (1).png"
        size_hint: 0.86,0.86
        pos_hint: {'center_x' :0.5, 'center_y' :0.43}
    MDRectangleFlatButton:
        text: 'LABORATORY MANUAL'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "25sp"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        size_hint: 0.82,0.185
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.show_MDDialog()
    Image:
        source: "LAB MANUALS (1).png"
        size_hint: 0.86,0.86
        pos_hint: {'center_x' :0.5, 'center_y' :0.2}
                    
<ExamScreen>:
    name: 'examcs'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'examtt'
    MDLabel:
        text: 'Computer'
        pos_hint: {'center_x' :0.5, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDLabel:
        text: 'Science'
        pos_hint: {'center_x' :0.45, 'center_y' :0.88}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<ExamttScreen>:
    name: 'examtt'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes'  
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'opt'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "EE1.png"
        size_hint: 2.3,2.3
        pos_hint: {'center_x' :0.5, 'center_y' :0.92}
    Image:
        source: "DOODLE 720 1446 .png"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ttmath'
        Image:
            source: "math-book.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ttchem'
        Image:
            source: "science.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ttphy'
        Image:
            source: "physics.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'examcs'
        Image:
            source: "coding.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ttec'
        Image:
            source: "cpu.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ttmech'
        Image:
            source: "piston.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ttcivil'
        Image:
            source: "civil.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ttaiml'
        Image:
            source: "AIML.png"
            size_hint: 0.60,0.60
    
<TtmathScreen>:
    name: 'ttmath'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'examtt'
    MDLabel:
        text: 'Mathematics'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    
        
<TtchemScreen>:
    name: 'ttchem'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'examtt'
    MDLabel:
        text: 'Chemistry'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'

<TtphyScreen>:
    name: 'ttphy'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'examtt'
    MDLabel:
        text: 'Physics'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<TtecScreen>:
    name: 'ttec'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'examtt'
    MDLabel:
        text: 'Electronics &'
        pos_hint: {'center_x' :0.5, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '25sp'
    MDLabel:
        text: 'Communication'
        pos_hint: {'center_x' :0.5, 'center_y' :0.88}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "25sp"
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<TtmechScreen>:
    name: 'ttmech'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'examtt'
    MDLabel:
        text: 'Mechanical'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<TtcivilScreen>:
    name:'ttcivil'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'examtt'
    MDLabel:
        text: 'Civil'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<TtaimlScreen>:
    name:'ttaiml'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'examtt'
    MDLabel:
        text: 'Artificial Intelligence &'
        pos_hint: {'center_x' :0.5, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '20sp'
    MDLabel:
        text: 'Machine Learning'
        pos_hint: {'center_x' :0.5, 'center_y' :0.88}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "25sp"
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
            
<QuemainScreen>:
    name: 'quemain'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes'  
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'opt'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "DOODLE 720 1446 .png"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
    Image:
        source: "QQ1.png"
        size_hint: 2.3,2.3
        pos_hint: {'center_x' :0.5, 'center_y' :0.93}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'qmath'
        Image:
            source: "math-book.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'qchem'
        Image:
            source: "science.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'qphy'
        Image:
            source: "physics.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'question'
        Image:
            source: "coding.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'qec'
        Image:
            source: "cpu.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'qmech'
        Image:
            source: "piston.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'qcivil'
        Image:
            source: "civil.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'qaiml'
        Image:
            source: "AIML.png"
            size_hint: 0.60,0.60       

<QueScreen>:
    name: 'question'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'quemain'
    MDLabel:
        text: 'Computer'
        pos_hint: {'center_x' :0.55, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '50sp'
    MDLabel:
        text: 'Science'
        pos_hint: {'center_x' :0.4, 'center_y' :0.88}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<QuemathScreen>:
    name: 'qmath'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'quemain'
    MDLabel:
        text: 'Mathematics'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    
        
<QuechemScreen>:
    name: 'qchem'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'quemain'
    MDLabel:
        text: 'Chemistry'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'

<QuephyScreen>:
    name: 'qphy'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'quemain'
    MDLabel:
        text: 'Physics'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<QueecScreen>:
    name: 'qec'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'quemain'
    MDLabel:
        text: 'Electronics &'
        pos_hint: {'center_x' :0.5, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '25sp'
    MDLabel:
        text: 'Communication'
        pos_hint: {'center_x' :0.5, 'center_y' :0.88}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "25sp"
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<QuemechScreen>:
    name: 'qmech'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'quemain'
    MDLabel:
        text: 'Mechanical'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<QuecivilScreen>:
    name:'qcivil'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'quemain'
    MDLabel:
        text: 'Civil'
        pos_hint: {'center_x' :0.5, 'center_y' :0.89}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '35sp'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<QueaimlScreen>:
    name:'qaiml'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'quemain'
    MDLabel:
        text: 'Artificial Intelligence &'
        pos_hint: {'center_x' :0.5, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'Button'
        font_size: '20sp'
    MDLabel:
        text: 'Machine Learning'
        pos_hint: {'center_x' :0.5, 'center_y' :0.88}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "25sp"
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.23, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.74}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.69}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<VideoScreen>
    name: 'video'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'opt'
    MDLabel:
        text: 'Videos'
        pos_hint: {'center_x' :0.55, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.1
        font_style : 'Button'
        font_size: '80sp'
    MDLabel:
        text: 'Videos'
        pos_hint: {'center_x' :0.35, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    ScrollView:
        do_scroll_x: True
        pos_hint: {'center_x':0.48,'center_y':0.82}
        size_hint: 1,0.07
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: None
            width: 2150
            padding: "20dp"
            spacing: "20dp"
            MDRectangleFlatButton:
                text: '3rd Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
            MDRectangleFlatButton:
                text: '4th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs4v'
            MDRectangleFlatButton:
                text: '5th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs5v'
            MDRectangleFlatButton:
                text: '6th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs6v'
            MDRectangleFlatButton:
                text: '7th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs7v'
            MDRectangleFlatButton:
                text: '8th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs8v'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.43}
        size_hint: 1,0.68
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2000
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Data Structure And Applications'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1  
                on_release: app.launch_link(0) 
            MDRectangleFlatButton:
                text: 'Analog And Digital Electronics'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(1)
            MDRectangleFlatButton:
                text: 'Computer Organization'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(2)
            MDRectangleFlatButton:
                text: 'Software Engineering'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(3)
            MDRectangleFlatButton:
                text: 'Discrete Mathematical Structure'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(4)
                
<OptScreen>:
    name: 'opt'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes' 
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'opt'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "DOODLE 720 1446 .png"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "math-book.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.72}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "science.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "physics.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'video'
        Image:
            source: "coding.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "cpu.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "piston.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "civil.png"
            size_hint: 0.60,0.60
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        Image:
            source: "AIML.png"
            size_hint: 0.60,0.60
    MDLabel:
        text: 'Videos'
        pos_hint: {'center_x' :0.45, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.1
        font_style : 'Button'
        font_size: '80sp'
    MDLabel:
        text: 'Videos'
        pos_hint: {'center_x' :0.25, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
        
<CS4VScreen>:
    name: 'cs4v'
    MDLabel:
        text: 'Videos'
        pos_hint: {'center_x' :0.45, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.1
        font_style : 'Button'
        font_size: '80sp'
    MDLabel:
        text: '4th SEM'
        pos_hint: {'center_x' :0.3, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    ScrollView:
        do_scroll_x: True
        pos_hint: {'center_x':0.48,'center_y':0.82}
        size_hint: 1,0.07
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: None
            width: 2150
            padding: "20dp"
            spacing: "20dp"
            MDRectangleFlatButton:
                text: '3rd Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'video'
            MDRectangleFlatButton:
                text: '4th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs4v'
            MDRectangleFlatButton:
                text: '5th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs5v'
            MDRectangleFlatButton:
                text: '6th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs6v'
            MDRectangleFlatButton:
                text: '7th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs7v'
            MDRectangleFlatButton:
                text: '8th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs8v'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.43}
        size_hint: 1,0.68
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2000
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Design And Analysis Of Algorithm'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1 
                on_release: app.launch_link(5) 
            MDRectangleFlatButton:
                text: 'Operating Systems'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(6)
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(7)
                MDLabel:
                    text: 'Microcontroller And Embedded Systems' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'OOP Concepts'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(8)
            MDRectangleFlatButton:
                text: 'Data Communication'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(9)
                
<CS5VScreen>:
    name: 'cs5v'
    MDLabel:
        text: 'Videos'
        pos_hint: {'center_x' :0.45, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.1
        font_style : 'Button'
        font_size: '80sp'
    MDLabel:
        text: '5th SEM'
        pos_hint: {'center_x' :0.3, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    ScrollView:
        do_scroll_x: True
        pos_hint: {'center_x':0.48,'center_y':0.82}
        size_hint: 1,0.07
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: None
            width: 2150
            padding: "20dp"
            spacing: "20dp"
            MDRectangleFlatButton:
                text: '3rd Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'video'
            MDRectangleFlatButton:
                text: '4th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs4v'
            MDRectangleFlatButton:
                text: '5th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs5v'
            MDRectangleFlatButton:
                text: '6th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs6v'
            MDRectangleFlatButton:
                text: '7th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs7v'
            MDRectangleFlatButton:
                text: '8th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs8v'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.43}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2400
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1 
                on_release: app.launch_link(130)
                MDLabel:
                    text: 'Management And Entrepreneurship For IT Industry' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Computer Networks And Security'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(131)
            MDRectangleFlatButton:
                text: 'Database Management System'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(132)
            MDRectangleFlatButton:
                text: 'Automata Theory And Computability'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(133)
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(134)
                MDLabel:
                    text: 'Application Development Using Python' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'UNIX Programming'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(135)

<CS6VScreen>:
    name: 'cs6v'
    MDLabel:
        text: 'Videos'
        pos_hint: {'center_x' :0.45, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.1
        font_style : 'Button'
        font_size: '80sp'
    MDLabel:
        text: '6th SEM'
        pos_hint: {'center_x' :0.3, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    ScrollView:
        do_scroll_x: True
        pos_hint: {'center_x':0.48,'center_y':0.82}
        size_hint: 1,0.07
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: None
            width: 2150
            padding: "20dp"
            spacing: "20dp"
            MDRectangleFlatButton:
                text: '3rd Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'video'
            MDRectangleFlatButton:
                text: '4th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs4v'
            MDRectangleFlatButton:
                text: '5th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs5v'
            MDRectangleFlatButton:
                text: '6th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs6v'
            MDRectangleFlatButton:
                text: '7th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs7v'
            MDRectangleFlatButton:
                text: '8th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs8v'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.43}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 3200
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1  
                on_release: app.launch_link(136)
                MDLabel:
                    text: 'System Software And Compiler Design' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button' 
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(137)
                MDLabel:
                    text: 'Computer Graphics And Visualization' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'SMS'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(138)
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(139)
                MDLabel:
                    text: 'Web Technology And Application' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Cloud Computing'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(140)
            MDRectangleFlatButton:
                text: 'Advanced JAVA'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(141)
            MDRectangleFlatButton:
                text: 'DMW'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(142)
            MDRectangleFlatButton:
                text: 'SCM'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_release: app.launch_link(143)
                
<CS7VScreen>:
    name: 'cs7v'
    MDLabel:
        text: 'Videos'
        pos_hint: {'center_x' :0.45, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.1
        font_style : 'Button'
        font_size: '80sp'
    MDLabel:
        text: '7th SEM'
        pos_hint: {'center_x' :0.3, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    ScrollView:
        do_scroll_x: True
        pos_hint: {'center_x':0.48,'center_y':0.82}
        size_hint: 1,0.07
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: None
            width: 2150
            padding: "20dp"
            spacing: "20dp"
            MDRectangleFlatButton:
                text: '3rd Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'video'
            MDRectangleFlatButton:
                text: '4th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs4v'
            MDRectangleFlatButton:
                text: '5th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs5v'
            MDRectangleFlatButton:
                text: '6th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs6v'
            MDRectangleFlatButton:
                text: '7th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs7v'
            MDRectangleFlatButton:
                text: '8th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs8v'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.68}
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(144)
        MDLabel:
            text: 'Artificial Intelligence And Machine Learning' 
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            font_size: "18sp"
            font_style: 'Button'
    MDRectangleFlatButton:
        text: 'Big Data Analytics'
        pos_hint: {'center_x':0.5,'center_y':0.53}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(145)
        
<CS8VScreen>:
    name: 'cs8v'
    MDLabel:
        text: 'Videos'
        pos_hint: {'center_x' :0.45, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.1
        font_style : 'Button'
        font_size: '80sp'
    MDLabel:
        text: '8th SEM'
        pos_hint: {'center_x' :0.3, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    ScrollView:
        do_scroll_x: True
        pos_hint: {'center_x':0.48,'center_y':0.82}
        size_hint: 1,0.07
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: None
            width: 2150
            padding: "20dp"
            spacing: "20dp"
            MDRectangleFlatButton:
                text: '3rd Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'video'
            MDRectangleFlatButton:
                text: '4th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs4v'
            MDRectangleFlatButton:
                text: '5th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs5v'
            MDRectangleFlatButton:
                text: '6th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs6v'
            MDRectangleFlatButton:
                text: '7th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs7v'
            MDRectangleFlatButton:
                text: '8th Sem'
                pos_hint: {'center_x' :0.7, 'center_y' :0.83}
                halign:'center'
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style : 'Button'
                font_size: "15sp"
                on_press: root.manager.current = 'cs8v'
    MDRectangleFlatButton:
        text: 'Internet Of Things'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(146)
    MDRectangleFlatButton:
        text: 'NO SQL'
        pos_hint: {'center_x':0.5,'center_y':0.53}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(147)
    MDRectangleFlatButton:
        text: 'SAN'
        pos_hint: {'center_x':0.5,'center_y':0.38}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(148)
                
<ShareScreen>:
    name: 'share'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes'
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'opt'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "Adobe_Express_20221014_2110410_1.png"
        size_hint: 0.60,0.60
        pos_hint: {'center_x' :0.8, 'center_y' :0.9}
    Image:
        source: "DOODLE 720 1446 .png"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
    MDLabel:
        text: 'SHARE'
        pos_hint: {'center_x' :0.22, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'H5'
    MDLabel:
        text: 'SHARE'
        pos_hint: {'center_x' :0.22, 'center_y' :0.9}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,1
        font_style : 'H5'
    MDLabel:
        text: 'SHARE'
        pos_hint: {'center_x' :0.22, 'center_y' :0.87}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.3
        font_style : 'H5'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.7}
        size_hint: 0.85,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint: 0.85,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(149)
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.3}
        size_hint: 0.85,0.16
        md_bg_color: 159/255,0/255,255/255,1
    MDLabel:
        text: 'REACH  OUT  TO  US'
        pos_hint: {'center_x' :0.5, 'center_y' :0.16}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "20sp"
    MDLabel:
        text: 'Discussion'
        pos_hint: {'center_x' :0.31, 'center_y' :0.7}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "20sp"
    Image:
        source: "chat.png"
        size_hint: 0.22,0.22
        pos_hint: {'center_x' :0.77, 'center_y' :0.7}
    MDLabel:
        text: 'REPORT A BUG'
        pos_hint: {'center_x' :0.35, 'center_y' :0.5}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "20sp"
    Image:
        source: "bug.png"
        size_hint: 0.22,0.22
        pos_hint: {'center_x' :0.77, 'center_y' :0.5}
    MDLabel:
        text: 'RATE US'
        pos_hint: {'center_x' :0.28, 'center_y' :0.3}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "20sp"
    Image:
        source: "top-rated.png"
        size_hint: 0.22,0.22
        pos_hint: {'center_x' :0.77, 'center_y' :0.3}
        
<NotesScreen>:
    name: 'notes'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes'
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'opt'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "DOODLE 720 1446 .png"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
    MDLabel:
        text: 'NOTES'
        pos_hint: {'center_x' :0.45, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.1
        font_style : 'Button'
        font_size: '90sp'
    MDLabel:
        text: 'NOTES'
        pos_hint: {'center_x' :0.22, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    MDRectangleFlatButton:
        text: '18SCHEME'
        pos_hint: {'center_x' :0.3, 'center_y' :0.83}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "15sp"
        on_press: root.manager.current = 'notes'
    MDRectangleFlatButton:
        text: '21SCHEME'
        pos_hint: {'center_x' :0.7, 'center_y' :0.83}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "15sp"
        on_press: root.manager.current = 'notes1'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.44}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 3000
            padding: "20dp"
            spacing: "20dp"
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.8,0.13
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'math'
                Image:
                    source: "math-book.png"
                    size_hint: 0.60,0.60
                    pos_hint: {'center_x' :0.9, 'center_y' :0.73}
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.67}
                size_hint: 0.8,0.13
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'computer'
                Image:
                    source: "coding.png"
                    size_hint: 0.60,0.60
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.67}
                size_hint: 0.8,0.13
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'electronics'
                Image:
                    source: "cpu.png"
                    size_hint: 0.60,0.60
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.67}
                size_hint: 0.8,0.13
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "piston.png"
                    size_hint: 0.60,0.60
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.67}
                size_hint: 0.8,0.13
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "civil.png"
                    size_hint: 0.60,0.60
                    
<Notes1Screen>:
    name: 'notes1'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes'
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'opt'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "DOODLE 720 1446 .png"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
    MDLabel:
        text: 'NOTES'
        pos_hint: {'center_x' :0.45, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 159/255,0/255,255/255,0.1
        font_style : 'Button'
        font_size: '90sp'
    MDLabel:
        text: 'NOTES'
        pos_hint: {'center_x' :0.22, 'center_y' :0.93}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "35sp"
    MDRectangleFlatButton:
        text: '18SCHEME'
        pos_hint: {'center_x' :0.3, 'center_y' :0.83}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "15sp"
        on_press: root.manager.current = 'notes'
    MDRectangleFlatButton:
        text: '21SCHEME'
        pos_hint: {'center_x' :0.7, 'center_y' :0.83}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
        font_size: "15sp"
        on_press: root.manager.current = 'notes1'
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.44}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 4200
            padding: "20dp"
            spacing: "20dp"
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.8,0.31
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "math-book.png"
                    size_hint: 0.60,0.60
                    pos_hint: {'center_x' :0.9, 'center_y' :0.73}
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.8,0.31
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "science.png"
                    size_hint: 0.60,0.60
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.8,0.31
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "physics.png"
                    size_hint: 0.60,0.60
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.67}
                size_hint: 0.8,0.31
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "coding.png"
                    size_hint: 0.60,0.60
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.67}
                size_hint: 0.8,0.31
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "cpu.png"
                    size_hint: 0.60,0.60
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.67}
                size_hint: 0.8,0.31
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "piston.png"
                    size_hint: 0.60,0.60
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.67}
                size_hint: 0.8,0.31
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "civil.png"
                    size_hint: 0.60,0.60
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.67}
                size_hint: 0.8,0.31
                md_bg_color: 159/255,0/255,255/255,1
                Image:
                    source: "AIML.png"
                    size_hint: 0.60,0.60
             
<CSScreen>:
    name: 'computer'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'notes'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes' 
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'video'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "CSE Card.png"
        size_hint: 2,2
        pos_hint: {'center_x' :0.5, 'center_y' :0.79}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'cs3'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'cs4'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'cs5'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'cs6'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'cs7'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'cs8'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'

<CS3Screen>:
    name: 'cs3'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'computer'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2000
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Data Structure And Applications'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1 
                on_press: root.manager.current = 'DS'  
            MDRectangleFlatButton:
                text: 'Analog And Digital Electronics'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'ADE'
            MDRectangleFlatButton:
                text: 'Computer Organization'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'CO'
            MDRectangleFlatButton:
                text: 'Software Engineering'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'SE'
            MDRectangleFlatButton:
                text: 'Discrete Mathematical Structure'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1  
                on_press: root.manager.current = 'DMS'

<CS4Screen>:
    name: 'cs4'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'computer'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2000
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Design And Analysis Of Algorithm'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1 
                on_press: root.manager.current = 'DAA'  
            MDRectangleFlatButton:
                text: 'Operating Systems'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'OS'
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'MES'
                MDLabel:
                    text: 'Microcontroller And Embedded Systems' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'OOP Concepts'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'OOP'
            MDRectangleFlatButton:
                text: 'Data Communication'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'DC'

<CS5Screen>:
    name: 'cs5'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'computer'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2400
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1 
                on_press: root.manager.current = 'MEI'
                MDLabel:
                    text: 'Management And Entrepreneurship For IT Industry' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Computer Networks And Security'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'CNS'
            MDRectangleFlatButton:
                text: 'Database Management System'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'DBMS'
            MDRectangleFlatButton:
                text: 'Automata Theory And Computability'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'ATC'
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'ADP'
                MDLabel:
                    text: 'Application Development Using Python' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'UNIX Programming'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'UNIX'
        
<CS6Screen>:
    name: 'cs6'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'computer'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 3200
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1  
                on_press: root.manager.current = 'SSC'
                MDLabel:
                    text: 'System Software And Compiler Design' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button' 
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'CGV'
                MDLabel:
                    text: 'Computer Graphics And Visualization' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'SMS'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'SMS'
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'WTA'
                MDLabel:
                    text: 'Web Technology And Application' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Cloud Computing'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'CC'
            MDRectangleFlatButton:
                text: 'Advanced JAVA'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'AJ'
            MDRectangleFlatButton:
                text: 'DMW'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'DMW'
            MDRectangleFlatButton:
                text: 'SCM'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'SCM'
        
<CS7Screen>:
    name: 'cs7'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'computer'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.5,'center_y':0.68}
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'AIML'
        MDLabel:
            text: 'Artificial Intelligence And Machine Learning' 
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            font_size: "18sp"
            font_style: 'Button'
    MDRectangleFlatButton:
        text: 'Big Data Analytics'
        pos_hint: {'center_x':0.5,'center_y':0.53}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'BD'
        
<CS8Screen>:
    name: 'cs8'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'computer'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'Internet Of Things'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'IOT'
    MDRectangleFlatButton:
        text: 'NO SQL'
        pos_hint: {'center_x':0.5,'center_y':0.53}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'SQL'
    MDRectangleFlatButton:
        text: 'SAN'
        pos_hint: {'center_x':0.5,'center_y':0.38}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.82,0.12
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'SAN'
        
<DSScreen>:
    name: 'DS'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(10)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(11)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(12)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(13)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(14)
        
<ADEScreen>:
    name: 'ADE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(15)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(16)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(17)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(18)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(19)      
    
<COScreen>:
    name: 'CO'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(20)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(21)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(22)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(23)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(24)
        
<SEScreen>:
    name: 'SE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(25)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(26)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(27)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(28)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(29)
        
<DMSScreen>:
    name: 'DMS'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(30)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(31)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(32)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(33)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(34)
    
<DAAScreen>:
    name: 'DAA'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(35)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(36)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(37)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(38)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(39)
        
<OSScreen>:
    name: 'OS'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(40)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(41)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(42)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(43)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1    
        on_release: app.launch_link(44)  
    
<MESScreen>:
    name: 'MES'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(45) 
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(46) 
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(47) 
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(48) 
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(49) 
        
<OOPScreen>:
    name: 'OOP'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(50)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(51)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(52)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(53)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(54)
        
<DCScreen>:
    name: 'DC'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(55)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(56)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(57)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(58)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(59)

<MEIScreen>:
    name: 'MEI'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(60)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(61)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(62)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(63)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(64)
        
<CNSScreen>:
    name: 'CNS'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(65)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(66)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(67)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(68)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(69)
        
<DBMSScreen>:
    name: 'DBMS'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(70)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(71)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(72)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(73)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(74)
        
<ATCScreen>:
    name: 'ATC'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(75)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(76)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(77)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(78)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(79)
        
<ADPScreen>:
    name: 'ADP'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(80)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(81)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(82)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(83)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(84)
        
<UNIXScreen>:
    name: 'UNIX'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(85)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(86)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(87)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(88)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(89)
        
<SSCScreen>:
    name: 'SSC'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(90)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(91)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(92)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(93)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(94)
        
<CGVScreen>:
    name: 'CGV'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(95)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(96)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(97)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(98)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(99)
        
<SMSScreen>:
    name: 'SMS'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        
<WTAScreen>:
    name: 'WTA'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(100)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(101)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(102)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(103)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(104)
        
<CCScreen>:
    name: 'CC'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1

<AJScreen>:
    name: 'AJ'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        
<DMWScreen>:
    name: 'DMW'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(105)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(106)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(107)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(108)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(109)
        
<SCMScreen>:
    name: 'SCM'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        
<AIMLScreen>:
    name: 'AIML'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs7'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(110)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(111)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(112)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(113)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(114)
        
<BDScreen>:
    name: 'BD'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs7'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(115)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(116)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(117)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(118)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(119)
        
<IOTScreen>:
    name: 'IOT'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs8'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(120)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(121)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(122)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(123)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(124)
        
<SQLScreen>:
    name: 'SQL'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs8'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        
<SANScreen>:
    name: 'SAN'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'cs8'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(125)
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(126)
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(127)
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(128)
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        on_release: app.launch_link(129)
        
<ECScreen>:
    name: 'electronics'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'notes'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes' 
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'video'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "EC.png"
        size_hint: 2,2
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ec3'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ec4'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ec5'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.36}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ec6'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ec7'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.18}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'ec8'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '5'
        pos_hint: {'center_x' :0.15, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '6'
        pos_hint: {'center_x' :0.65, 'center_y' :0.38}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.33}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '7'
        pos_hint: {'center_x' :0.15, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '8'
        pos_hint: {'center_x' :0.65, 'center_y' :0.2}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.15}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        
<EC3Screen>:
    name: 'ec3'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'electronics'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2000
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Network Theory'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'NT'   
            MDRectangleFlatButton:
                text: 'Electronic Devices'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'ED'
            MDRectangleFlatButton:
                text: 'Digital System Design'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'DSD'
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'COA'
                MDLabel:
                    text: 'Computer Organization and architecture' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Power Electronics and Instruction'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1  
                on_press: root.manager.current = 'PSI'

<EC4Screen>:
    name: 'ec4'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'electronics'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2000
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Analog Circuits'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1 
                on_press: root.manager.current = 'AC'  
            MDRectangleFlatButton:
                text: 'Control Systems'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'CSE'
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'ESLM'
                MDLabel:
                    text: 'Engineering statistics and linear methods' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Signals and systems'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'SS'
            MDRectangleFlatButton:
                text: 'Micro Controller'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1  
                on_press: root.manager.current = 'MC'
                
<EC5Screen>:
    name: 'ec5'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'electronics'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2300
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'time'
                MDLabel:
                    text: 'Technological innovation management and entrepreneurship' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'  
            MDRectangleFlatButton:
                text: 'Digital signal processing'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'dsp'
            MDRectangleFlatButton:
                text: 'Principles of communication'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'pac'
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'itc'
                MDLabel:
                    text: 'Information theory and coding' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Electromagnetic waves'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'wc'
            MDRectangleFlatButton:
                text: 'VHDL'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'vhdl'
                
<EC6Screen>:
    name: 'ec6'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'electronics'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2950
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Digital communication'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1 
                on_press: root.manager.current = 'DCE'  
            MDRectangleFlatButton:
                text: 'Embedded systems'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'ESE'
            MDRectangleFlatButton:
                text: 'Microwave and antennas'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'MAA'
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'DSUV'
                MDLabel:
                    text: 'Digital system using verilog' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Operating system'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'OSE'
            MDRectangleFlatButton:
                text: 'Python application programming'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'PAPE'
            MDRectangleFlatButton:
                text: 'Artificial neural network'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'ANNE'
            MDRectangleFlatButton:
                text: 'JAVA'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'JAVAE'
                
<EC7Screen>:
    name: 'ec7'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'electronics'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2000
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                text: 'Computer networks'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1   
                on_press: root.manager.current = 'CNE'
            MDRectangleFlatButton:
                text: 'Cryptography'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'CE'
            MDRectangleFlatButton:
                text: 'Real time systems'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'RTSE'
            MDRectangleFlatButton:
                text: 'Satellite communication'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'SCE'
            MDRectangleFlatButton:
                text: 'VLSI'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'VLSIE'
                
<EC8Screen>:
    name: 'ec8'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'electronics'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    ScrollView:
        do_scroll_y: True
        pos_hint: {'center_x':0.5,'center_y':0.41}
        size_hint: 1,0.7
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 2000
            padding: "20dp"
            spacing: "25dp"
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'WCCE'
                MDLabel:
                    text: 'Wireless and cellular communication' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button' 
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'OCNE'
                MDLabel:
                    text: 'Optical communication and network' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Network security'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'NSE'
            MDRectangleFlatButton:
                pos_hint: {'center_x':0.5,'center_y':0.73}
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'MEMSE'
                MDLabel:
                    text: 'Micro electro mechanical systems' 
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_size: "18sp"
                    font_style: 'Button'
            MDRectangleFlatButton:
                text: 'Power Electronics and Instruction'
                pos_hint: {'center_x':0.5,'center_y':0.73}
                theme_text_color: "Custom"
                text_color: 1,1,1,1
                font_size: "18sp"
                font_style: 'Button'
                size_hint: 0.9,0.31
                md_bg_color: 159/255,0/255,255/255,1
                on_press: root.manager.current = 'PEAIE'
                
<NTScreen>:
    name: 'NT'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<EDScreen>:
    name: 'ED'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<EScreen>:
    name: 'ED'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<DSDScreen>:
    name: 'DSD'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<COAScreen>:
    name: 'COA'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<PSIScreen>:
    name: 'PSI'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec3'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1

<ACScreen>:
    name: 'AC'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<CSEScreen>:
    name: 'CSE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<ESLMScreen>:
    name: 'ESLM'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<SSScreen>:
    name: 'SS'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<MCScreen>:
    name: 'MC'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec4'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<TIMEScreen>:
    name: 'time'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<DSPScreen>:
    name: 'dsp'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<PACScreen>:
    name: 'pac'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<ITCScreen>:
    name: 'itc'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<WCScreen>:
    name: 'wc'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<VHDLScreen>:
    name: 'vhdl'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec5'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<DCEScreen>:
    name: 'DCE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<ESEScreen>:
    name: 'ESE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<MAAScreen>:
    name: 'MAA'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<DSUVScreen>:
    name: 'DSUV'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<OSEScreen>:
    name: 'OSE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<PAPEScreen>:
    name: 'PAPE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<ANNEScreen>:
    name: 'ANNE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<JAVAEScreen>:
    name: 'JAVAE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec6'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<CNEScreen>:
    name: 'CNE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec7'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<CEScreen>:
    name: 'CE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec7'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<RTSEScreen>:
    name: 'RTSE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec7'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<SCEScreen>:
    name: 'SCE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec7'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<VLSIEScreen>:
    name: 'VLSIE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec7'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<WCCEScreen>:
    name: 'WCCE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec8'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<OCNEScreen>:
    name: 'OCNE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec8'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<NSEScreen>:
    name: 'NSE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec8'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<MEMSEScreen>:
    name: 'MEMSE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec8'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<PEAIEScreen>:
    name: 'PEAIE'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'ec8'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        
<MathScreen>:
    name: 'math'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'notes'
    MDIconButton:
        icon: 'home-outline'
        pos_hint:{'center_x' :0.14, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'menu'
    MDIconButton:
        icon: 'apps'
        pos_hint:{'center_x' :0.36, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'notes' 
    MDIconButton:
        icon: 'play-box-outline'
        pos_hint:{'center_x' :0.62, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1  
        on_press: root.manager.current = 'video'    
    MDIconButton:
        icon: 'share-variant-outline'
        pos_hint:{'center_x' :0.84, 'center_y' :0.04}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1
        on_press: root.manager.current = 'share'
    Image:
        source: "MATH.png"
        size_hint: 2,2
        pos_hint: {'center_x' :0.5, 'center_y' :0.77}
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'm1'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.54}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'm2'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.26,'center_y':0.34}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'm3'
    MDRectangleFlatButton:
        pos_hint: {'center_x':0.74,'center_y':0.34}
        size_hint: 0.4,0.16
        md_bg_color: 159/255,0/255,255/255,1
        on_press: root.manager.current = 'm4'
    MDLabel:
        text: '1'
        pos_hint: {'center_x' :0.15, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '2'
        pos_hint: {'center_x' :0.65, 'center_y' :0.56}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '3'
        pos_hint: {'center_x' :0.15, 'center_y' :0.36}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.22, 'center_y' :0.31}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
    MDLabel:
        text: '4'
        pos_hint: {'center_x' :0.65, 'center_y' :0.36}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
        font_size: "50sp"
    MDLabel:
        text: 'Semester'
        pos_hint: {'center_x' :0.71, 'center_y' :0.3}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_style : 'Button'
<M1Screen>:
    name: 'm1'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'math'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<M2Screen>:
    name: 'm2'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'math'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<M3Screen>:
    name: 'm3'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'math'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
<M4Screen>:
    name: 'm4'
    MDIconButton:
        icon: 'chevron-double-left'
        pos_hint:{'center_x' :0.09, 'center_y' :0.96}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 0,0,0,1 
        on_press: root.manager.current = 'math'
    Image:
        source: "My project-1 (1).png"
        size_hint: 0.8,0.8
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRectangleFlatButton:
        text: 'MODULE - 1'
        pos_hint: {'center_x':0.5,'center_y':0.68}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 2'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 3'
        pos_hint: {'center_x':0.5,'center_y':0.42}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 4'
        pos_hint: {'center_x':0.5,'center_y':0.29}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
    MDRectangleFlatButton:
        text: 'MODULE - 5'
        pos_hint: {'center_x':0.5,'center_y':0.16}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: "18sp"
        font_style: 'Button'
        size_hint: 0.9,0.1
        md_bg_color: 159/255,0/255,255/255,1
        
"""

class MenuScreen(Screen):
    pass

class ExamScreen(Screen):
    pass

class QueScreen(Screen):
    pass

class VideoScreen(Screen):
    pass

class ShareScreen(Screen):
    pass

class NotesScreen(Screen):
    pass

class Notes1Screen(Screen):
    pass

class CSScreen(Screen):
    pass

class CS3Screen(Screen):
    pass

class CS4Screen(Screen):
    pass

class CS5Screen(Screen):
    pass

class CS6Screen(Screen):
    pass

class CS7Screen(Screen):
    pass

class CS8Screen(Screen):
    pass

class DSScreen(Screen):
    pass

class ADEScreen(Screen):
    pass

class COScreen(Screen):
    pass

class SEScreen(Screen):
    pass

class DMSScreen(Screen):
    pass

class DAAScreen(Screen):
    pass

class OSScreen(Screen):
    pass

class MESScreen(Screen):
    pass

class OOPScreen(Screen):
    pass

class DCScreen(Screen):
    pass

class MEIScreen(Screen):
    pass

class CNSScreen(Screen):
    pass

class DBMSScreen(Screen):
    pass

class ATCScreen(Screen):
    pass

class ADPScreen(Screen):
    pass

class UNIXScreen(Screen):
    pass

class SSCScreen(Screen):
    pass

class CGVScreen(Screen):
    pass

class SMSScreen(Screen):
    pass

class WTAScreen(Screen):
    pass

class CCScreen(Screen):
    pass

class AJScreen(Screen):
    pass

class DMWScreen(Screen):
    pass

class SCMScreen(Screen):
    pass

class AIMLScreen(Screen):
    pass

class BDScreen(Screen):
    pass

class IOTScreen(Screen):
    pass

class SQLScreen(Screen):
    pass

class SANScreen(Screen):
    pass

class CS4VScreen(Screen):
    pass

class CS5VScreen(Screen):
    pass

class CS6VScreen(Screen):
    pass

class CS7VScreen(Screen):
    pass

class CS8VScreen(Screen):
    pass

class ECScreen(Screen):
    pass

class EC3Screen(Screen):
    pass

class EC4Screen(Screen):
    pass

class EC5Screen(Screen):
    pass

class EC6Screen(Screen):
    pass

class EC7Screen(Screen):
    pass

class EC8Screen(Screen):
    pass

class NTScreen(Screen):
    pass

class EDScreen(Screen):
    pass

class DSDScreen(Screen):
    pass

class COAScreen(Screen):
    pass

class PSIScreen(Screen):
    pass

class ACScreen(Screen):
    pass

class CSEScreen(Screen):
    pass

class ESLMScreen(Screen):
    pass

class SSScreen(Screen):
    pass

class MCScreen(Screen):
    pass

class MathScreen(Screen):
    pass

class TIMEScreen(Screen):
    pass

class DSPScreen(Screen):
    pass

class PACScreen(Screen):
    pass

class ITCScreen(Screen):
    pass

class WCScreen(Screen):
    pass

class VHDLScreen(Screen):
    pass

class DCEScreen(Screen):
    pass

class ESEScreen(Screen):
    pass

class MAAScreen(Screen):
    pass

class DSUVScreen(Screen):
    pass

class OSEScreen(Screen):
    pass

class PAPEScreen(Screen):
    pass

class ANNEScreen(Screen):
    pass

class JAVAEScreen(Screen):
    pass

class CNEScreen(Screen):
    pass

class CEScreen(Screen):
    pass

class RTSEScreen(Screen):
    pass

class SCEScreen(Screen):
    pass

class VLSIEScreen(Screen):
    pass

class WCCEScreen(Screen):
    pass

class OCNEScreen(Screen):
    pass

class NSEScreen(Screen):
    pass

class MEMSEScreen(Screen):
    pass

class PEAIEScreen(Screen):
    pass

class M1Screen(Screen):
    pass

class M2Screen(Screen):
    pass

class M3Screen(Screen):
    pass

class M4Screen(Screen):
    pass

class OptScreen(Screen):
    pass

class ExamttScreen(Screen):
    pass

class QuemainScreen(Screen):
    pass

class TtmathScreen(Screen):
    pass

class TtchemScreen(Screen):
    pass

class TtphyScreen(Screen):
    pass

class TtecScreen(Screen):
    pass

class TtmechScreen(Screen):
    pass

class TtcivilScreen(Screen):
    pass

class TtaimlScreen(Screen):
    pass

class QuemathScreen(Screen):
    pass

class QuechemScreen(Screen):
    pass

class QuephyScreen(Screen):
    pass

class QueecScreen(Screen):
    pass

class QuemechScreen(Screen):
    pass

class QuecivilScreen(Screen):
    pass

class QueaimlScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ExamScreen(name='exam'))
sm.add_widget(QueScreen(name='question'))
sm.add_widget(VideoScreen(name='saved'))
sm.add_widget(ShareScreen(name='share'))
sm.add_widget(NotesScreen(name='notes'))
sm.add_widget(Notes1Screen(name='notes1'))
sm.add_widget(CSScreen(name='computer'))
sm.add_widget(CS3Screen(name='CS3'))
sm.add_widget(CS4Screen(name='cs4'))
sm.add_widget(CS5Screen(name='cs5'))
sm.add_widget(CS6Screen(name='cs6'))
sm.add_widget(CS7Screen(name='cs7'))
sm.add_widget(CS8Screen(name='cs8'))
sm.add_widget(DSScreen(name='DS'))
sm.add_widget(ADEScreen(name='ADE'))
sm.add_widget(COScreen(name='CO'))
sm.add_widget(SEScreen(name='SE'))
sm.add_widget(DMSScreen(name='DMS'))
sm.add_widget(DAAScreen(name='DAA'))
sm.add_widget(OSScreen(name='OS'))
sm.add_widget(MESScreen(name='MES'))
sm.add_widget(OOPScreen(name='OOP'))
sm.add_widget(DCScreen(name='DC'))
sm.add_widget(MEIScreen(name='MEI'))
sm.add_widget(CNSScreen(name='CNS'))
sm.add_widget(DBMSScreen(name='DBMS'))
sm.add_widget(ATCScreen(name='ATC'))
sm.add_widget(ADPScreen(name='ADP'))
sm.add_widget(UNIXScreen(name='UNIX'))
sm.add_widget(SSCScreen(name='SSC'))
sm.add_widget(CGVScreen(name='CGV'))
sm.add_widget(SMSScreen(name='SMS'))
sm.add_widget(WTAScreen(name='WTA'))
sm.add_widget(CCScreen(name='CC'))
sm.add_widget(AJScreen(name='AJ'))
sm.add_widget(DMWScreen(name='DMW'))
sm.add_widget(SCMScreen(name='SCM'))
sm.add_widget(AIMLScreen(name='AIML'))
sm.add_widget(BDScreen(name='BD'))
sm.add_widget(IOTScreen(name='IOT'))
sm.add_widget(SQLScreen(name='SQL'))
sm.add_widget(SANScreen(name='SAN'))
sm.add_widget(CS4VScreen(name='cs4v'))
sm.add_widget(CS5VScreen(name='cs5v'))
sm.add_widget(CS6VScreen(name='cs6v'))
sm.add_widget(CS7VScreen(name='cs7v'))
sm.add_widget(CS8VScreen(name='cs8v'))
sm.add_widget(ECScreen(name='electronics'))
sm.add_widget(EC3Screen(name='ec3'))
sm.add_widget(EC4Screen(name='ec4'))
sm.add_widget(EC5Screen(name='ec5'))
sm.add_widget(EC6Screen(name='ec6'))
sm.add_widget(EC7Screen(name='ec7'))
sm.add_widget(EC8Screen(name='ec8'))
sm.add_widget(NTScreen(name='NT'))
sm.add_widget(EDScreen(name='ED'))
sm.add_widget(DSDScreen(name='DSD'))
sm.add_widget(COAScreen(name='COA'))
sm.add_widget(PSIScreen(name='PSI'))
sm.add_widget(ACScreen(name='AC'))
sm.add_widget(CSEScreen(name='CSE'))
sm.add_widget(ESLMScreen(name='ESLM'))
sm.add_widget(SSScreen(name='SS'))
sm.add_widget(MCScreen(name='MC'))
sm.add_widget(MathScreen(name='math'))
sm.add_widget(TIMEScreen(name='TIME'))
sm.add_widget(DSPScreen(name='DSP'))
sm.add_widget(PACScreen(name='PAC'))
sm.add_widget(ITCScreen(name='ITC'))
sm.add_widget(WCScreen(name='EW'))
sm.add_widget(VHDLScreen(name='VHDL'))
sm.add_widget(DCEScreen(name='DCE'))
sm.add_widget(ESEScreen(name='ESE'))
sm.add_widget(MAAScreen(name='MAA'))
sm.add_widget(DSUVScreen(name='DSUV'))
sm.add_widget(OSEScreen(name='OSE'))
sm.add_widget(PAPEScreen(name='PAPE'))
sm.add_widget(ANNEScreen(name='ANNE'))
sm.add_widget(JAVAEScreen(name='JAVAE'))
sm.add_widget(CNEScreen(name='CNE'))
sm.add_widget(CEScreen(name='CE'))
sm.add_widget(RTSEScreen(name='RTSE'))
sm.add_widget(SCEScreen(name='SCE'))
sm.add_widget(VLSIEScreen(name='VLSIE'))
sm.add_widget(WCCEScreen(name=' WCCE'))
sm.add_widget(OCNEScreen(name='OCNE'))
sm.add_widget(NSEScreen(name='NSE'))
sm.add_widget(MEMSEScreen(name='MEMSE'))
sm.add_widget(PEAIEScreen(name='PEAIE'))
sm.add_widget(M1Screen(name='m1'))
sm.add_widget(M2Screen(name='m2'))
sm.add_widget(M3Screen(name='m3'))
sm.add_widget(M4Screen(name='m4'))
sm.add_widget(OptScreen(name='opt'))
sm.add_widget(ExamttScreen(name='examtt'))
sm.add_widget(QuemainScreen(name='quemain'))
sm.add_widget(TtmathScreen(name='ttmath'))
sm.add_widget(TtchemScreen(name='ttchem'))
sm.add_widget(TtphyScreen(name='ttphy'))
sm.add_widget(TtecScreen(name='ttec'))
sm.add_widget(TtmechScreen(name='ttmech'))
sm.add_widget(TtcivilScreen(name='ttcivil'))
sm.add_widget(TtaimlScreen(name='Ttaiml'))
sm.add_widget(QuemathScreen(name='qmath'))
sm.add_widget(QuechemScreen(name='qchem'))
sm.add_widget(QuephyScreen(name='qphy'))
sm.add_widget(TtecScreen(name='qec'))
sm.add_widget(QuemechScreen(name='qmech'))
sm.add_widget(QuecivilScreen(name='qcivil'))
sm.add_widget(QueaimlScreen(name='qaiml'))

class GeekNotesApp(MDApp):

    def build(self):
        self.icon = "Adobe_Express_20221014_2110410_1.png"
        screen = Builder.load_string(screen_helper)
        return screen

    def show_MDDialog(self):
        close_button = MDFlatButton(text= 'Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title = 'Laboratory Manual', text = 'Laboratory Manual Will Be Released On New Update', auto_dismiss = False, buttons=[close_button])
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def launch_link(self, index):
        link = ''
        if index == 0:
            link = 'https://youtube.com/playlist?list=PLdo5W4Nhv31bbKJzrsKfMpo_grxuLl8LU'
        elif index == 1:
            link = 'https://youtube.com/playlist?list=PLrBwg460eks8CYGT6j5S-KEY2q_HVhnNk'
        elif index == 2:
            link = 'https://youtube.com/playlist?list=PLBlnK6fEyqRgLLlzdgiTUKULKJPYc0A4q'
        elif index == 3:
            link = 'https://youtube.com/playlist?list=PLrjkTql3jnm9b5nr-ggx7Pt1G4UAHeFlJ'
        elif index == 4:
            link = 'https://youtube.com/playlist?list=PLU6SqdYcYsfJ27O0dvuMwafS3X8CecqUg'
        elif index == 5:
            link = 'https://youtube.com/playlist?list=PLxCzCOWd7aiHcmS4i14bI0VrMbZTUvlTa'
        elif index == 6:
            link = 'https://youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O'
        elif index == 7:
            link = 'https://youtube.com/playlist?list=PLrjkTql3jnm8HbdMwBYIMAd3UdstWChFH'
        elif index == 8:
            link = 'https://youtube.com/playlist?list=PL-DlK9z03yoih9u_9FaD0LCc2lhysTaaY'
        elif index == 9:
            link = 'https://youtube.com/playlist?list=PLcwp2fRcIXJW0UsZlUgZCYJSqCS23GUsp'
        elif index == 10:
            link = 'https://drive.google.com/file/d/167zCWGpRgNY9fzH_myBKzM1YRDhangYa/view?usp=share_link'
        elif index == 11:
            link = 'https://drive.google.com/file/d/1NrkyQ38UbURNksv_mH2DlOXN58rVgeRm/view?usp=share_link'
        elif index == 12:
            link = 'https://drive.google.com/file/d/1clgB2PY-TSg43gZMXGOwXLFi0mJEs8UC/view?usp=share_link'
        elif index == 13:
            link = 'https://drive.google.com/file/d/1Ne3olArYNUP05DEX94t1HuNb74zaLc3t/view?usp=share_link'
        elif index == 14:
            link = 'https://drive.google.com/file/d/1SdYZYkG09bzOCD7AEXF-Z-sF_BX2F0Zs/view?usp=share_link'
        elif index == 15:
            link = 'https://drive.google.com/file/d/1Cc2Ym3V77Ac2sl2mLTCHxYiOfE1HR9wp/view?usp=share_link'
        elif index == 16:
            link = 'https://drive.google.com/file/d/1myycewxKPOBfWiJvQLGRTbzo3lMA5SRa/view?usp=share_link'
        elif index == 17:
            link = 'https://drive.google.com/file/d/1ZGBHJjGCAGpM0T1vdHsu-knpkTj9vnHq/view?usp=share_link'
        elif index == 18:
            link = 'https://drive.google.com/file/d/159xAWs5WfS5t7hy8dXI-iO2O049rk06C/view?usp=share_link'
        elif index == 19:
            link = 'https://drive.google.com/file/d/1S8SIxfgd87oBXrOmh8qbj-lT8RRdgQtv/view?usp=share_link'
        elif index == 20:
            link = 'https://drive.google.com/file/d/1pAUYbAAo9PPK0NZpCfoLFZFbkAOVKqbM/view?usp=share_link'
        elif index == 21:
            link = 'https://drive.google.com/file/d/1Iuq7czzF_diTxKBNXZFV3IhWPWZd6420/view?usp=share_link'
        elif index == 22:
            link = 'https://drive.google.com/file/d/1F1E0uL9ajfNZQFIgqymRWxB13GMqTP8g/view?usp=share_link'
        elif index == 23:
            link = 'https://drive.google.com/file/d/1-gcF7TVjPzm_LrpfIc3glQZ5vY3NCYEt/view?usp=share_link'
        elif index == 24:
            link = 'https://drive.google.com/file/d/1UdNNy3Byd9r-JNvr5n_fj3jekE2ZtvEm/view?usp=share_link'
        elif index == 25:
            link = 'https://drive.google.com/file/d/1kBj0yBF3TvtmKG49NVfH4lVVKDfSyKF2/view?usp=share_link'
        elif index == 26:
            link = 'https://drive.google.com/file/d/1vFua0Dwa-H2eOKNW74Ws-byXNLkmP5WS/view?usp=share_link'
        elif index == 27:
            link = 'https://drive.google.com/file/d/1fh2sVW8wsvyXLHxT24uDpZIlPvcIWQIG/view?usp=share_link'
        elif index == 28:
            link = 'https://drive.google.com/file/d/1hXga-3eiZ2_9tTdP8U2XE7brhhMN6mkp/view?usp=share_link'
        elif index == 29:
            link = 'https://drive.google.com/file/d/1gROgCAx9n6mqbYfnFJwb84PUCV0uVC9-/view?usp=share_link'
        elif index == 30:
            link = 'https://drive.google.com/file/d/1EomXyaxdQy6SjkSee-jLClGPtPo1yp-5/view?usp=share_link'
        elif index == 31:
            link = 'https://drive.google.com/file/d/14u_ptVwCUcZeRbKpApHlM3eDYzZmTrR8/view?usp=share_link'
        elif index == 32:
            link = 'https://drive.google.com/file/d/1rRtJv7eqpRbtcACdTfnrBeA7E5r7EPCw/view?usp=share_link'
        elif index == 33:
            link = 'https://drive.google.com/file/d/1FeRFUzZNjeR-mtteQA4AmyzI9i9cAtM4/view?usp=share_link'
        elif index == 34:
            link = 'https://drive.google.com/file/d/1cry-jA5MdkPzjJpuLqxXc0n2SVS9voRO/view?usp=share_link'
        elif index == 35:
            link = 'https://drive.google.com/file/d/1MUyxzH6AWFJTVJRKgYFm4Us01QkT4e1H/view?usp=share_link'
        elif index == 36:
            link = 'https://drive.google.com/file/d/16RJUh_12N4FEkr3huQktj8qUpDA8AIDj/view?usp=share_link'
        elif index == 37:
            link = 'https://drive.google.com/file/d/10icjXsy7y3Q2-OcYsFEtoDRjTQiF8h1_/view?usp=share_link'
        elif index == 38:
            link = 'https://drive.google.com/file/d/1Z6_nEg94dU82lFXcNftQcJ6wKfQyBZQg/view?usp=share_link'
        elif index == 39:
            link = 'https://drive.google.com/file/d/16FFT1Emovdj_PIreS3cwnOZ9rylIDBiE/view?usp=share_link'
        elif index == 40:
            link = 'https://drive.google.com/file/d/1o-tDKXrS074bK7eWJLTlv2erMMihCKcQ/view?usp=share_link'
        elif index == 41:
            link = 'https://drive.google.com/file/d/1NwHX-zGbALPDsTUfuycV5XQRQRxAl34V/view?usp=share_link'
        elif index == 42:
            link = 'https://drive.google.com/file/d/1A-KdG4ghhByoFLrK6qPKgK0-c2Xz8F37/view?usp=share_link'
        elif index == 43:
            link = 'https://drive.google.com/file/d/15gfX0yum_2cwW42bCw_9pbbUabPOVwJN/view?usp=share_link'
        elif index == 44:
            link = 'https://drive.google.com/file/d/1rUiRsWm8U5aqrF6c_mmdWX9oypM_C9p1/view?usp=share_link'
        elif index == 45:
            link = 'https://drive.google.com/file/d/1eSxO9lDrixAoY-oVcV_qL3sJvSUVxIg3/view?usp=share_link'
        elif index == 46:
            link = 'https://drive.google.com/file/d/1vBA4BJEkC46DeQTzUE-S3kIFYqsaH4ea/view?usp=share_link'
        elif index == 47:
            link = 'https://drive.google.com/file/d/1tghY8J-OKO6PbDQF2Vqli6SWhUuB896T/view?usp=share_link'
        elif index == 48:
            link = 'https://drive.google.com/file/d/16a-ras_thgIMwF2DpQHkNBHtFJ-LyWDI/view?usp=share_link'
        elif index == 49:
            link = 'https://drive.google.com/file/d/1i_hBu41KSxu7aJxBBwOC4-8Z5ULYs2FO/view?usp=share_link'
        elif index == 50:
            link = 'https://drive.google.com/file/d/1cbgw6nbQyu_aO1sfX787MPV5DD7I6jBT/view?usp=share_link'
        elif index == 51:
            link = 'https://drive.google.com/file/d/18dD3pJeOabEqQ7upsKQ5vqsjAsAzQrAX/view?usp=share_link'
        elif index == 52:
            link = 'https://drive.google.com/file/d/1NRq8Uf6emejKkK_9fHycmC0lzwSnqbdN/view?usp=share_link'
        elif index == 53:
            link = 'https://drive.google.com/file/d/1yD-vM1lW7kaT9yPqfEMN0lYVxKNvLSMz/view?usp=share_link'
        elif index == 54:
            link = 'https://drive.google.com/file/d/1KumA3NLOzRjEFK3a_HmJFjXTnMdfxSwW/view?usp=share_link'
        elif index == 55:
            link = 'https://drive.google.com/file/d/1n6FjRQYo-HluCW6wUR_OX88j-7BsJPQF/view?usp=share_link'
        elif index == 56:
            link = 'https://drive.google.com/file/d/1RopvFexMpehBsYbQbXpJnWPxh8Bs3-SZ/view?usp=share_link'
        elif index == 57:
            link = 'https://drive.google.com/file/d/1GZPhSQMFP_n6Ey28PANlGq0UWby4dgxt/view?usp=share_link'
        elif index == 58:
            link = 'https://drive.google.com/file/d/1xEzs7oWMF86ZKT_Mfbf0aeAO-8NKHtH9/view?usp=share_link'
        elif index == 59:
            link = 'https://drive.google.com/file/d/1kiEojvtiiXN3A9pKWihk91aHcks5mVSp/view?usp=share_link'
        elif index == 60:
            link = 'https://drive.google.com/file/d/1qiNhntq7q-z_VSvuoRelx0rRxNIM2LvC/view?usp=share_link'
        elif index == 61:
            link = 'https://drive.google.com/file/d/1upon7zx08E2uPPC1VcCrjHVsz8SrdSbf/view?usp=share_link'
        elif index == 62:
            link = 'https://drive.google.com/file/d/1eENurHcrKI55E3eX6cMRWyT75zk5kjpo/view?usp=share_link'
        elif index == 63:
            link = 'https://drive.google.com/file/d/1MWQ5LaiSYp8gOVe3DjplGQfJrYOwXV_-/view?usp=share_link'
        elif index == 64:
            link = 'https://drive.google.com/file/d/19eonYITuyV65mG9e_qoXGvnSmGYUt17x/view?usp=share_link'
        elif index == 65:
            link = 'https://drive.google.com/file/d/1ka56QpfP-yAK3VVbiuHobes7jyat2Kz2/view?usp=share_link'
        elif index == 66:
            link = 'https://drive.google.com/file/d/1quHLDrGjiFqNEWGpMiz1xWa5fvHh3Eo4/view?usp=share_link'
        elif index == 67:
            link = 'https://drive.google.com/file/d/1bZYGvNUx-tqOYEaXw15AzQnh3CQf7Oig/view?usp=share_link'
        elif index == 68:
            link = 'https://docs.google.com/document/d/1gOrCABAeGYov4sHUP0L8bN0sQuZ_Wi-g/edit?usp=share_link&ouid=118318599272781239739&rtpof=true&sd=true'
        elif index == 69:
            link = 'https://docs.google.com/document/d/1gOrCABAeGYov4sHUP0L8bN0sQuZ_Wi-g/edit?usp=share_link&ouid=118318599272781239739&rtpof=true&sd=true'
        elif index == 70:
            link = 'https://drive.google.com/file/d/1W9U0YZb4uoi7GK-ke7TYaXyTi9JSINnm/view?usp=share_link'
        elif index == 71:
            link = 'https://drive.google.com/file/d/10pgYL_PfB5uNybBhrUO-Lxt3KqtNLj9k/view?usp=share_link'
        elif index == 72:
            link = 'https://drive.google.com/file/d/1wB9IqlCtXR6nOUOCV02NreQrhRVf-NVe/view?usp=share_link'
        elif index == 73:
            link = 'https://drive.google.com/file/d/11YP_8LgSlYWRLzN4ZfbGq5alQbAMjLDs/view?usp=share_link'
        elif index == 74:
            link = 'https://drive.google.com/file/d/1Pr6UclE_1u9FToLzBdqfZTXfb0_ABuxy/view?usp=share_link'
        elif index == 75:
            link = 'https://drive.google.com/file/d/1bYyCv-8pZjUP1lklwCHLHMkZsdBijIwI/view?usp=share_link'
        elif index == 76:
            link = 'https://drive.google.com/file/d/1vyRH0GCQKSNclxNhp35Ox0iFTfICnyxG/view?usp=share_link'
        elif index == 77:
            link = 'https://drive.google.com/file/d/1x2TUjut7GF0vhhkoMl5fS-XUwzkKfGgg/view?usp=share_link'
        elif index == 78:
            link = 'https://drive.google.com/file/d/1MeFNXku8USctgo6dHFM-CSQ6q2dIpMny/view?usp=share_link'
        elif index == 79:
            link = 'https://drive.google.com/file/d/1A6jWWS49eTdroAEKGneAOUFr75HcDLRZ/view?usp=share_link'
        elif index == 80:
            link = 'https://drive.google.com/file/d/1jiIk3d7QwCf4NZrFEOCsgESo8e4ee1Xg/view?usp=share_link'
        elif index == 81:
            link = 'https://drive.google.com/file/d/1GepxBr2w-jme1CrMqztmdJcEi1ml-gAP/view?usp=share_link'
        elif index == 82:
            link = 'https://drive.google.com/file/d/1zXDvSg9e_Y4_26JKgfWH9vRZGgwGOutr/view?usp=share_link'
        elif index == 83:
            link = 'https://drive.google.com/file/d/10kzkMNjdSRhk7VjAH1mCppCYwSCXVkSV/view?usp=share_link'
        elif index == 84:
            link = 'https://drive.google.com/file/d/11zezISbgHlvco4zIyiVcK9yXi1xHE1T3/view?usp=share_link'
        elif index == 85:
            link = 'https://drive.google.com/file/d/1pkxKAr6tTpzrFiS_NXnsGvayBeh8ddjc/view?usp=share_link'
        elif index == 86:
            link = 'https://drive.google.com/file/d/1Y14nZhTwwfjOEKK8PmuUwcTKZJKgOf8A/view?usp=share_link'
        elif index == 87:
            link = 'https://drive.google.com/file/d/1Jgcm6siXjZxV6VgYx2ZqdRFC3IvxZgll/view?usp=share_link'
        elif index == 88:
            link = 'https://drive.google.com/file/d/1WlfCL_8Rh7yAWQ7pT8lzexeRfTlikSPE/view?usp=share_link'
        elif index == 89:
            link = 'https://drive.google.com/file/d/1BVMHjq3f9fHJQ4W8LvYNaIynrLwWNEjp/view?usp=share_link'
        elif index == 90:
            link = 'https://drive.google.com/file/d/1re5LvalXKHPWCE_bebbfFzU-K4mHDK98/view?usp=share_link'
        elif index == 91:
            link = 'https://drive.google.com/file/d/1RYUcmgJKTd-aWnZ9U9zgaE9xm65CvhZj/view?usp=share_link'
        elif index == 92:
            link = 'https://drive.google.com/file/d/1JhTkQZUCLuawacLe3CcqNDFURfif-qJ7/view?usp=share_link'
        elif index == 93:
            link = 'https://drive.google.com/file/d/1SOsXJib1tqrj3sq6zIOLERT742m8zuWY/view?usp=share_link'
        elif index == 94:
            link = 'https://drive.google.com/file/d/1jnB2CT8G2Ji82yJSjnjDgx4cQ20nksus/view?usp=share_link'
        elif index == 95:
            link = 'https://drive.google.com/file/d/1jDjWLs4XurEf2cRqrZHAm0ZQEbjJaZqj/view?usp=share_link'
        elif index == 96:
            link = 'https://drive.google.com/file/d/1vrwJC19ARHiSKJhB_cgICtTA1YKBKJEP/view?usp=share_link'
        elif index == 97:
            link = 'https://drive.google.com/file/d/1CQb1RSEM0oaxyDSJ6jIRO0PIlabC1Bqd/view?usp=share_link'
        elif index == 98:
            link = 'https://drive.google.com/file/d/1JvJR_vrn-g0Y46MOREjMWoR669a5_qAt/view?usp=share_link'
        elif index == 99:
            link = 'https://drive.google.com/file/d/1hLdEVkXyPHKbOxKfLmroIZF6wIPb7G1J/view?usp=share_link'
        elif index == 100:
            link = 'https://drive.google.com/file/d/1rTpbiJnqGXroHlQ9X1_W_QTaTCndSrea/view?usp=share_link'
        elif index == 101:
            link = 'https://drive.google.com/file/d/10xoS3W-jfLvsCuqpT1h9UHRdn2EKUspa/view?usp=share_link'
        elif index == 102:
            link = 'https://drive.google.com/file/d/1NxeC6luIqnBkuN9-Oaoqktw3ELz66Q0u/view?usp=share_link'
        elif index == 103:
            link = 'https://drive.google.com/file/d/13XXS3sl8C9b5SqOIFRIuWGtex1TJZElz/view?usp=share_link'
        elif index == 104:
            link = 'https://drive.google.com/file/d/1Mnoi5W52QgOrW2rsyVyORLP3zt29XwWq/view?usp=share_link'
        elif index == 105:
            link = 'https://drive.google.com/file/d/1TjD_jbax45wN-DFmwmsBw7a3yUbXXcOc/view?usp=share_link'
        elif index == 106:
            link = 'https://drive.google.com/file/d/1On7IragZ14TpTfONzpw25kz2ASu_bfxo/view?usp=share_link'
        elif index == 107:
            link = 'https://drive.google.com/file/d/1SAVxINncS3C9dT4AUia_cMIAzn79KSX6/view?usp=share_link'
        elif index == 108:
            link = 'https://drive.google.com/file/d/1Ve_i_SxpAyOwVRtJdmoc4o_HFMgrPkUz/view?usp=share_link'
        elif index == 109:
            link = 'https://drive.google.com/file/d/1uoAhaQtl8J5POhHxC7Km_KY-_7UYCuOZ/view?usp=share_link'
        elif index == 110:
            link = 'https://drive.google.com/file/d/1d_8ac41iv2ImKtx01xgyrBBDgPTTRTa-/view?usp=share_link'
        elif index == 111:
            link = 'https://drive.google.com/file/d/1F8yRPTzkaZ65edNJvx4BED4n1yrb7OfX/view?usp=share_link'
        elif index == 112:
            link = 'https://drive.google.com/file/d/1aUpcrjWp_fQrdljHUJb0g2OJJhcHMMz1/view?usp=share_link'
        elif index == 113:
            link = 'https://drive.google.com/file/d/104xYvcHsPde4Mr9mJ_Mh32aQGBnG7AQc/view?usp=share_link'
        elif index == 114:
            link = 'https://drive.google.com/file/d/1TEtxJwJXRmFiAkDGOaNJoJ8xw0xDCdBG/view?usp=share_link'
        elif index == 115:
            link = 'https://drive.google.com/file/d/1PTRhsvzsnyuW-OwSuH0wongx3DpZ9xy2/view?usp=share_link'
        elif index == 116:
            link = 'https://drive.google.com/file/d/1wY08OokbqBp9cUokYHOGGqB04Y83FzzP/view?usp=share_link'
        elif index == 117:
            link = 'https://drive.google.com/file/d/1qLCMNJfqr8BHxIpYvHb7cy8ycivb__rt/view?usp=share_link'
        elif index == 118:
            link = 'https://drive.google.com/file/d/1KQTFaW8X3fCCc-zSJxex3C0AxcurWl0i/view?usp=share_link'
        elif index == 119:
            link = 'https://drive.google.com/file/d/1Je_S8L5cklohU7gcADNUlVzH2yBNp6cY/view?usp=share_link'
        elif index == 120:
            link = 'https://drive.google.com/file/d/12UYWnM2qfs9DS3sPM4Iej1ypLrWaYxPk/view?usp=share_link'
        elif index == 121:
            link = 'https://drive.google.com/file/d/189I0tWjVAfiv7oOsexbGyd80AQHWHtfV/view?usp=share_link'
        elif index == 122:
            link = 'https://drive.google.com/file/d/1lM12pGGECK72pNWOnPurTPLKNpCQ0tHm/view?usp=share_link'
        elif index == 123:
            link = 'https://drive.google.com/file/d/1kXzycAW3JCuBjhBM5in9KJXeb5sAqAxN/view?usp=share_link'
        elif index == 124:
            link = 'https://drive.google.com/file/d/1p7E5HFn-u6KaV9g9AZrYaW5A0BXk-OLV/view?usp=share_link'
        elif index == 125:
            link = 'https://drive.google.com/file/d/1ds5TEZRDwG73tuRAX0DlzfjJSoiQvYPD/view?usp=share_link'
        elif index == 126:
            link = 'https://drive.google.com/file/d/1abDQjiPG8EFhn4MMzl5Pzoi1iFL9dU1e/view?usp=share_link'
        elif index == 127:
            link = 'https://drive.google.com/file/d/1bIlaXNOYN5N9MbN7qiz8Q5JtFMT-3fS3/view?usp=share_link'
        elif index == 128:
            link = 'https://drive.google.com/file/d/1VRuV9Sk6FnXZEINY0Xo-g4AdlvsMX1nE/view?usp=share_link'
        elif index == 129:
            link = 'https://drive.google.com/file/d/1ooT0NnOQi1cl0okRMYqTFvlElkhD2gnh/view?usp=share_link'
        elif index == 130:
            link = 'https://youtube.com/playlist?list=PLaWv8T8DVaywyGkuwHWDKFbtUw32BZgD_'
        elif index == 131:
            link = 'https://youtube.com/playlist?list=PLBlnK6fEyqRgMCUAG0XRw78UA8qnv6jEx'
        elif index == 132:
            link = 'https://youtube.com/playlist?list=PLBlnK6fEyqRi_CUQ-FXxgzKQ1dwr_ZJWZ'
        elif index == 133:
            link = 'https://youtube.com/playlist?list=PLOZyfu4IYm8-RWzdAbF-ZKEYXmD_2LUWI'
        elif index == 134:
            link = 'https://youtube.com/playlist?list=PLHNnptZlo-7-mfpMvoWLY3nOtVyMs_JCg'
        elif index == 135:
            link = 'https://youtube.com/playlist?list=PLOZyfu4IYm8_28oMh9cBP-duLJ2SdKYt6'
        elif index == 136:
            link = 'https://youtube.com/playlist?list=PLLkv5JJU3sIZuB-scsFSqZ7Dk4NZNRiHf'
        elif index == 137:
            link = 'https://youtube.com/playlist?list=PLrjkTql3jnm9cY0ijEyr2fPdwnH-0t8EY'
        elif index == 138:
            link = 'https://youtube.com/playlist?list=PLk_1WO51gohlbZVnun8ohxbLLi_9fhL-A'
        elif index == 139:
            link = 'https://youtube.com/playlist?list=PLrjkTql3jnm8d1ddpVKifXO_fPjSKATCp'
        elif index == 140:
            link = 'https://youtube.com/playlist?list=PLrjkTql3jnm86_Jr9195OaqN-HeiBy49I'
        elif index == 141:
            link = 'https://youtube.com/playlist?list=PLMl2dbGQSb_82wlWDJ4PXkOjDlpMbPiPt'
        elif index == 142:
            link = 'https://youtube.com/playlist?list=PL_XK0Lt9uR8PuN_UizgUrIlkGJs88r_64'
        elif index == 143:
            link = 'https://youtube.com/playlist?list=PLUHGprUixGhWi_sKEg43RB80P8gyniuTE'
        elif index == 144:
            link = 'https://youtube.com/playlist?list=PLrjkTql3jnm_yol-ZK1QqPSn5YSg0NF9r'
        elif index == 145:
            link = 'https://youtube.com/playlist?list=PLBBGwIiUvNPCML5y4WHRWPJn4zrzPS8dk'
        elif index == 146:
            link = 'https://youtube.com/playlist?list=PLVDfFatHsysRBoJP2dZftSjK80JEyDPE5'
        elif index == 147:
            link = 'https://youtube.com/playlist?list=PLsyeobzWxl7r0bn6dzVA8bQNxcx7DRl5F'
        elif index == 148:
            link = 'https://youtube.com/playlist?list=PL-g8c2TsJCfy8Im-8MMYt3f7OpfNtQu5P'
        elif index == 149:
            link = 'https://surveyheart.com/form/639c057bb482b4504c4d81c0'
        webbrowser.open(link)


if __name__ == "__main__":
    GeekNotesApp().run()