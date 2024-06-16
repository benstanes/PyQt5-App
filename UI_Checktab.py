from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QPushButton, QVBoxLayout, QCheckBox, QSlider
from PyQt5.uic import loadUi
import subprocess
import time

class HomeInitial(QDialog):
    def __init__(self):
        super(HomeInitial, self).__init__()
        loadUi("tabwidget_check.ui", self)

        # Connect the Initialize_button clicked signal to the launch_controller function
        self.initialize_button.clicked.connect(self.launch_controller)

    def launch_controller(self):
        # Define the commands to run in the new terminals
        controller_command = "roslaunch robot_controller automatoncontroller.launch"
        move_group_command = "roslaunch automaton_moveit move_group.launch"

        # Open the first terminal, run the first command
        self.open_terminal_and_run_command(controller_command)

        # Open the second terminal, run the second command
        self.open_terminal_and_run_command(move_group_command)
        self.event_log.setText("Automatron CORE configured, MOVE_GROUP Launched. You can start planning now!")
    def open_terminal_and_run_command(self, command, delay=5):
        try:
            # Open a new terminal window and execute the specified command
            subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

            # Wait for the terminal to fully open and the command to run
            time.sleep(delay)

        except Exception as e:
            print(f"Error: {str(e)}")

        # Connect the Enable_button clicked signal to the toggle_jogging_buttons function
        self.Enable_button.clicked.connect(self.toggle_jogging_buttons)
    def toggle_jogging_buttons(self):
        # Toggle the state of the specified buttons in the Jogging tab
        for button in self.jogging_buttons_to_enable:
            button.setEnabled(not button.isEnabled())

        # Disable and toggle JOG buttons when A1, LX, and EX are disabled
        if not self.A1.isEnabled() and not self.LX.isEnabled() and not self.EX.isEnabled():
            self.set_initial_JOG_buttons_state()

    def set_initial_JOG_buttons_state(self):
        # Set the initial state of the JOG buttons to disabled
        self.JOG1.setEnabled(False)
        self.JOG2.setEnabled(False)
        self.JOG3.setEnabled(False)

        # Define buttons in the Jogging tab to be enabled/disabled
        self.jogging_buttons_to_enable = [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.LX, self.LY, self.LZ, self.EX, self.EY, self.EZ, self.increment_1, self.increment_2, self.increment_3, 
                                          self.slider, self.slider_2, self.slider_3, self.slider_4, self.slider_5, self.slider_6, self.slider_7, self.slider_8, self.slider_9, self.slider_10, self.slider_11, self.slider_12]
        for button in self.jogging_buttons_to_enable:
            button.setEnabled(False)
    #     # Set the initial state of the jogging buttons (disabled)
    #     self.set_initial_jogging_buttons_state()

    # def set_initial_jogging_buttons_state(self):
    #     # Set the initial state of the specified buttons in the Jogging tab to disabled
      

        # Connect the A1, A2, A3 buttons clicked signals to the corresponding enable_JOG buttons functions
        self.A1.clicked.connect(lambda: self.JOG1.setEnabled(True))
        self.LX.clicked.connect(lambda: self.JOG2.setEnabled(True))
        self.EX.clicked.connect(lambda: self.JOG3.setEnabled(True))

        # Connect the enable_calibbutton clicked signal to the toggle_calibration_buttons function
        self.enable_calibbutton.clicked.connect(self.toggle_calibration_buttons)
    def toggle_calibration_buttons(self):
        # Toggle the state of the specified buttons in the Calibration tab
        for button in self.calibration_buttons_to_toggle:
            button.setEnabled(not button.isEnabled())

        # Define buttons in the Calibration tab to be enabled/disabled
        self.calibration_buttons_to_toggle = [
            self.callockj1_cal1, self.callockj2_cal1, self.callockj3_cal1,
            self.callockj4_cal1, self.callockj5_cal1, self.callockj6_cal1
        ]

    def set_initial_calibration_buttons_state(self):
        # Set the initial state of the specified buttons in the Calibration tab to disabled
        for button in self.calibration_buttons_to_toggle:
            button.setEnabled(False)

        # Connect the callockjX_cal1 buttons clicked signals to the corresponding enable_calibJX buttons functions
        self.callockj1_cal1.clicked.connect(lambda: self.calibJ1_cal1.setEnabled(not self.calibJ1_cal1.isEnabled()))
        self.callockj2_cal1.clicked.connect(lambda: self.calibJ2_cal1.setEnabled(not self.calibJ2_cal1.isEnabled()))
        self.callockj3_cal1.clicked.connect(lambda: self.calibJ3_cal1.setEnabled(not self.calibJ3_cal1.isEnabled()))
        self.callockj4_cal1.clicked.connect(lambda: self.calibJ4_cal1.setEnabled(not self.calibJ4_cal1.isEnabled()))
        self.callockj5_cal1.clicked.connect(lambda: self.calibJ5_cal1.setEnabled(not self.calibJ5_cal1.isEnabled()))
        self.callockj6_cal1.clicked.connect(lambda: self.calibJ6_cal1.setEnabled(not self.calibJ6_cal1.isEnabled()))
        
    def set_initial_calibJX_cal1_buttons_state(self):
        # Set the initial state of the specified buttons in the Calibration tab to disabled
        self.calibJ1_cal1.setEnabled(False)
        self.calibJ2_cal1.setEnabled(False)
        self.calibJ3_cal1.setEnabled(False)
        self.calibJ4_cal1.setEnabled(False)
        self.calibJ5_cal1.setEnabled(False)
        self.calibJ6_cal1.setEnabled(False)

    def connect_jog_buttons_to_sliders(self):
        # Connect push_buttons in Jogging tab to enable sliders
        jog_buttons = [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.LX, self.LY, self.LZ, self.EX, self.EY, self.EZ]
        sliders = [
            self.slider, self.slider_2, self.slider_3, self.slider_4, self.slider_5,
            self.slider_6, self.slider_7, self.slider_8, self.slider_9, self.slider_10,
            self.slider_11, self.slider_12
        ]

        for button, slider in zip(jog_buttons, sliders):
            slider.setEnabled(False)  # Set sliders initially disabled
            button.clicked.connect(lambda state, s=slider: self.enable_slider(s))

    def enable_slider(self, slider):
        # Enable the slider when the corresponding button is clicked
        slider.setEnabled(True)

    def connect_line_edits_to_sliders(self):
        # Connect line edits to sliders for real-time updates
        line_edits = [
            self.text, self.text2, self.text3, self.text4, self.text5,
            self.text6, self.text7, self.text8, self.text9, self.text10,
            self.text11, self.text12
        ]
        sliders = [
            self.slider, self.slider_2, self.slider_3, self.slider_4, self.slider_5,
            self.slider_6, self.slider_7, self.slider_8, self.slider_9, self.slider_10,
            self.slider_11, self.slider_12
        ]

        for line_edit, slider in zip(line_edits, sliders):
            # Connect line edit's textChanged signal to update_slider_value method
            line_edit.textChanged.connect(lambda text, s=slider: self.update_slider_value(s, text))

            # Connect slider's valueChanged signal to update_line_edit_text method
            slider.valueChanged.connect(lambda value, le=line_edit: self.update_line_edit_text(le, value))

    def update_slider_value(self, slider, text):
        # Update the slider value when the corresponding line edit text changes
        try:
            value = float(text)
            slider.setValue(value)
        except ValueError:
            pass

    def update_line_edit_text(self, line_edit, value):
        # Update the line edit text when the corresponding slider value changes
        line_edit.setText(str(value))

    def connect_push_buttons_to_sliders(self):
        # Connect decrease and increase push buttons to sliders
        decrease_buttons = [
            self.decrease_1, self.decrease_2, self.decrease_3, self.decrease_4, self.decrease_5,
            self.decrease_6, self.decrease_7, self.decrease_8, self.decrease_9, self.decrease_10,
            self.decrease_11, self.decrease_12
        ]

        increase_buttons = [
            self.increase_1, self.increase_2, self.increase_3, self.increase_4, self.increase_5,
            self.increase_6, self.increase_7, self.increase_8, self.increase_9, self.increase_10,
            self.increase_11, self.increase_12
        ]

        sliders = [
            self.slider, self.slider_2, self.slider_3, self.slider_4, self.slider_5,
            self.slider_6, self.slider_7, self.slider_8, self.slider_9, self.slider_10,
            self.slider_11, self.slider_12
        ]

        for decrease_button, increase_button, slider in zip(decrease_buttons, increase_buttons, sliders):
            # Connect decrease button clicked signal to decrease_slider_value method
            decrease_button.clicked.connect(lambda _, s=slider: self.decrease_slider_value(s))
        
            # Connect increase button clicked signal to increase_slider_value method
            increase_button.clicked.connect(lambda _, s=slider: self.increase_slider_value(s))

    def decrease_slider_value(self, slider):
        # Decrease the slider value when the corresponding decrease button is clicked
        slider.setValue(slider.value() - 1)
    def increase_slider_value(self, slider):
        # Increase the slider value when the corresponding increase button is clicked
        slider.setValue(slider.value() + 1)

        # Connect enable_usermode button to toggle_usermode_buttons function
        self.enable_usermode.clicked.connect(self.toggle_usermode_buttons)
    def toggle_usermode_buttons(self):
        # Toggle the state of the specified buttons in the Program Editor User tab
        for button in self.usermode_buttons_to_toggle:
            button.setEnabled(not button.isEnabled())


        # Define buttons in Program Editor User tab to be enabled/toggled
        self.usermode_buttons_to_toggle = [
            self.add, self.modify, self.delete_2, self.verify
        ]

    def set_initial_usermode_buttons_state(self):
        # Set the initial state of the specified buttons in the Program Editor User tab to disabled
        for button in self.usermode_buttons_to_toggle:
            button.setEnabled(False)

        self.verify.clicked.connect(self.enable_verify_buttons)
    def enable_verify_buttons(self):
        # Enable the specified buttons in the Program Editor User tab when verify is clicked
        for button in self.verify_buttons_to_enable:
            button.setEnabled(True)

        # Define buttons in Program Editor User tab to be enabled when verify is clicked
        self.verify_buttons_to_enable = [
            self.prev, self.play, self.stop, self.next
        ]

    def set_initial_verify_buttons_state(self):
        # Set the initial state of the specified buttons in the Program Editor User tab to disabled
        for button in self.verify_buttons_to_enable:
            button.setEnabled(False)

       # Connect enable_AI button to toggle_AI_buttons function
        self.enable_AI.clicked.connect(self.toggle_AI_buttons)
    def toggle_AI_buttons(self):
        # Toggle the state of the specified buttons in the AI tab
        for button in self.AI_buttons_to_toggle:
            button.setEnabled(not button.isEnabled())

        # Define buttons in AI tab to be enabled/toggled
        self.AI_buttons_to_toggle = [
            self.front, self.back, self.up, self.down, self.left, self.right
        ]

    def set_initial_AI_buttons_state(self):
        # Set the initial state of the specified buttons in the AI tab to disabled
        for button in self.AI_buttons_to_toggle:
            button.setEnabled(False)

        # Connect buttons in AI tab to enable_up_buttons function
        self.front.clicked.connect(lambda: self.toggle_up_buttons("up1"))
        self.back.clicked.connect(lambda: self.toggle_up_buttons("up2"))
        self.up.clicked.connect(lambda: self.toggle_up_buttons("up3"))
        self.down.clicked.connect(lambda: self.toggle_up_buttons("up4"))
        self.left.clicked.connect(lambda: self.toggle_up_buttons("up5"))
        self.right.clicked.connect(lambda: self.toggle_up_buttons("up6"))

    def toggle_up_buttons(self, button_name):
        # Toggle the state of the specified up button in the AI tab
        for button in self.up_buttons_to_toggle:
            if button.objectName() == button_name:
                button.setEnabled(not button.isEnabled())

        # Define buttons in AI tab to be enabled/toggled by front, back, up, down, left, right buttons
        self.up_buttons_to_toggle = [
            self.up1, self.up2, self.up3, self.up4, self.up5, self.up6
        ]

    def set_initial_up_buttons_state(self):
        # Set the initial state of the specified buttons in the AI tab to disabled
        for button in self.up_buttons_to_toggle:
            button.setEnabled(False)

        self.enable_auto.clicked.connect(self.toggle_auto_buttons)
    def toggle_auto_buttons(self):
        # Toggle the state of the specified buttons in the Auto tab
        for button in self.auto_buttons_to_toggle:
            button.setEnabled(not button.isEnabled())

        # Define buttons in Auto tab to be enabled/toggled
        self.auto_buttons_to_toggle = [
            self.select, self.create, self.add_2, self.modify_2, self.delete_3, self.save_path
        ]

    def set_initial_auto_buttons_state(self):
        # Set the initial state of the specified buttons in the Auto tab to disabled
        for button in self.auto_buttons_to_toggle:
            button.setEnabled(False)

         # Connect save_path button to enable_add_delete_buttons function
        self.save_path.clicked.connect(self.enable_add_delete_buttons)
    def enable_add_delete_buttons(self):
        # Enable the specified buttons by save_path button
        for button in self.add_delete_buttons_to_enable:
            button.setEnabled(self.save_path.isEnabled())

        # Connect add_3 button to enable_load_prog_button function
        self.add_3.clicked.connect(self.enable_load_prog_button)
    def enable_load_prog_button(self):
        # Enable the specified buttons by add_3 button
        for button in self.load_prog_buttons_to_enable:
            button.setEnabled(True)

        # Connect load_prog button to enable_prog_buttons function
        self.load_prog.clicked.connect(self.enable_prog_buttons)
    def enable_prog_buttons(self):
        # Enable the specified buttons by load_prog button
        for button in self.prog_buttons_to_enable:
            button.setEnabled(True)

        # Define buttons to be enabled by save_path, add_3, load_prog buttons
        self.add_delete_buttons_to_enable = [
            self.add_3, self.delete_4
        ]

        # Define buttons to be enabled by add_3 button
        self.load_prog_buttons_to_enable = [
            self.load_prog
        ]

        # Define buttons to be enabled by load_prog button
        self.prog_buttons_to_enable = [
            self.prev_2, self.play_2, self.stop_2, self.next_2
        ]

    def set_initial_buttons_state(self):
        # Set the initial state of the specified buttons to disabled
        for button in self.add_delete_buttons_to_enable + self.load_prog_buttons_to_enable + self.prog_buttons_to_enable:
            button.setEnabled(False)

         # Connect enable_vis button to toggle_vis_buttons function
        self.enable_vis.clicked.connect(self.toggle_vis_buttons)
    def toggle_vis_buttons(self):
        # Toggle the state of the specified buttons in the Visualization tab
        for button in self.vis_buttons_to_toggle:
            button.setEnabled(not button.isEnabled())

        # Define buttons to be enabled/toggled by enable_vis button
        self.vis_buttons_to_toggle = [
            self.choose_path, self.choose_path_2, self.debug
        ]

    def set_initial_vis_buttons_state(self):
        # Set the initial state of the specified buttons in the Visualization tab to disabled
        for button in self.vis_buttons_to_toggle:
            button.setEnabled(False)

    def check_and_disable_up_buttons(self):
        # Check if all "front", "back", "up", "down", "left", "right" buttons are disabled
        if not any(button.isEnabled() for button in [self.front, self.back, self.up, self.down, self.left, self.right]):
            # Disable all "up" buttons
            for button in self.up_buttons_to_toggle:
                button.setEnabled(False)

    def gotohome(self):
        # Define the actions to perform when going to home
        pass  # Add your implementation here

if __name__ == "__main__":
    app = QApplication([])
    window = HomeInitial()
    window.show()
    app.exec_()
