from tkinter import Misc, StringVar, Tk, DoubleVar
from tkinter.ttk import Button, Entry, Label, OptionMenu, Labelframe, Checkbutton, Scale, Spinbox

import numpy as np

pars = {
    "Tonic Spiking": np.array([0.02, 0.2, -65, 6, 14]),
    "Phasic Spiking": np.array([0.02, 0.25, -65, 6, 0.5]),
    "Tonic Bursting": np.array([0.02, 0.2, -50, 2, 15]),
    "Phasic Bursting": np.array([0.02, 0.25, -55, 0.05, 0.6]),
    "Mixed Mode": np.array([0.02, 0.2, -55, 4, 10]),
    "Spike Frequency Adaptation": np.array([0.01, 0.2, -65, 8, 30]),
    "Class 1": np.array([0.02, -0.1, -55, 6, 0]),
    "Class 2": np.array([0.2, 0.26, -65, 0, 0]),
    "Spike Latency": np.array([0.02, 0.2, -65, 6, 7]),
    "Subthreshold Oscillations": np.array([0.05, 0.26, -60, 0, 0]),
    "Resonator": np.array([0.1, 0.26, -60, -1, 0]),
    "Integrator": np.array([0.02, -0.1, -55, 6, 0]),
    "Rebound Spike": np.array([0.03, 0.25, -60, 4, 0]),
    "Rebound Burst": np.array([0.03, 0.25, -52, 0, 0]),
    "Threshold Variability": np.array([0.03, 0.25, -60, 4, 0]),
    "Bistability": np.array([1, 1.5, -60, 0, -65]),
    "DAP": np.array([1, 0.2, -60, -21, 0]),
    "Accommodation": np.array([0.02, 1, -55, 4, 0]),
    "Inhibition Induced Spiking": np.array([-0.02, -1, -60, 8, 80]),
    "Inhibition Induced Bursting": np.array([-0.026, -1, -45, 0, 80]),
}


class SuperFrame(Labelframe):
    def __init__(self, parent: Misc, *args, **kwargs):
        super().__init__(parent, borderwidth=1, relief="ridge", padding=10, *args, **kwargs)


class InputCurrentFrame(SuperFrame):
    def __init__(self, parent: Misc):
        super().__init__(parent)


class ControlsFrame(SuperFrame):
    def __init__(self, parent: Misc):
        super().__init__(parent)

        self._paused = False
        self._pause_play_button = Button(self, text="Pause", command=self.pause_play)
        self._pause_play_button.pack()

        self._exit_button = Button(self, text="Exit", command=exit)
        self._exit_button.pack(pady=(20, 0))

        self._dt_value = DoubleVar()

        self._dt_entry = Spinbox(self)

        self._dt_slider = Scale(self, from_=0.001, to=10, variable=self._dt_value)
        self._dt_slider.pack()

    def pause_play(self):
        self._paused = not self._paused

        self._pause_play_button["text"] = "Resume" if self._paused else "Pause"

        # TODO: Callback


class ParameterFrame(SuperFrame):
    def __init__(self, parent: Misc):
        super().__init__(parent, text="Parameters")

        self._preset_value = StringVar(value=[*pars.keys()][0])
        self._a_value = StringVar()
        self._b_value = StringVar()
        self._c_value = StringVar()
        self._d_value = StringVar()
        self._I_value = StringVar()

        self._trace_lockout = False

        self._a_value.trace_add('write', lambda var, index, mode: self._clear_preset())
        self._b_value.trace_add('write', lambda var, index, mode: self._clear_preset())
        self._c_value.trace_add('write', lambda var, index, mode: self._clear_preset())
        self._d_value.trace_add('write', lambda var, index, mode: self._clear_preset())

        self._update_entries(self._preset_value.get())

        self._preset_label = Label(self, text="Preset")
        self._preset_entry = OptionMenu(self, self._preset_value, None, "--", *pars.keys(), command=self._update_entries)

        self._preset_entry.config(width=len(sorted([*pars.keys()], key=len, reverse=True)[0]))

        self._a_label = Label(self, text="a")
        self._a_entry = Entry(self, justify="right", textvariable=self._a_value)

        self._b_label = Label(self, text="b")
        self._b_entry = Entry(self, justify="right", textvariable=self._b_value)

        self._c_label = Label(self, text="c")
        self._c_entry = Entry(self, justify="right", textvariable=self._c_value)

        self._d_label = Label(self, text="d")
        self._d_entry = Entry(self, justify="right", textvariable=self._d_value)

        self._I_label = Label(self, text="I")
        self._I_entry = Entry(self, justify="right", textvariable=self._I_value)

        grid_settings = {"padx": 5, "pady": 5}

        self._preset_label.grid(row=0, column=0, sticky="E", **grid_settings)
        self._preset_entry.grid(row=0, column=1, sticky="WE", **grid_settings)

        self._a_label.grid(row=1, column=0, sticky="E", **grid_settings)
        self._a_entry.grid(row=1, column=1, sticky="WE", **grid_settings)

        self._b_label.grid(row=2, column=0, sticky="E", **grid_settings)
        self._b_entry.grid(row=2, column=1, sticky="WE", **grid_settings)

        self._c_label.grid(row=3, column=0, sticky="E", **grid_settings)
        self._c_entry.grid(row=3, column=1, sticky="WE", **grid_settings)

        self._d_label.grid(row=4, column=0, sticky="E", **grid_settings)
        self._d_entry.grid(row=4, column=1, sticky="WE", **grid_settings)

        self._I_label.grid(row=5, column=0, sticky="E", **grid_settings)
        self._I_entry.grid(row=5, column=1, sticky="WE", **grid_settings)

    def _update_entries(self, new_val: str):
        if new_val == "--":
            return
        
        params = pars[new_val]

        self._trace_lockout = True
        self._a_value.set(params[0])
        self._b_value.set(params[1])
        self._c_value.set(params[2])
        self._d_value.set(params[3])
        self._I_value.set(params[4])
        self._trace_lockout = False

    def _clear_preset(self):
        if not self._trace_lockout:
            self._preset_value.set('--')


class CurrentControls(SuperFrame):
    def __init__(self, parent: Misc):
        super().__init__(parent)

        self._exc_button = Button(self, text="Excitatory Pulse")
        self._inh_button = Button(self, text="Inhibitory Pulse")
        self._cont_button = Checkbutton(self, text="Continuous Current")

        self._exc_button.pack()
        self._inh_button.pack()
        self._cont_button.pack()


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Model by Izhikevich (2003)")
        self.geometry("1200x900")

        pack_params = {"padx": 5, "pady": 5}

        self._param_frame = ParameterFrame(self)
        self._param_frame.pack(side="left", **pack_params)

        self._controls_frame = ControlsFrame(self)
        self._controls_frame.pack(side="left", **pack_params)

        self._current_controls = CurrentControls(self)
        self._current_controls.pack(side="left", **pack_params)


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
