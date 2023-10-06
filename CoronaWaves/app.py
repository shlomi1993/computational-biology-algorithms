from tkinter import Tk, LabelFrame, Label, Entry, Canvas, Button, messagebox
from automata import Automata
from style import palette, fonts


def createEntry(master, default_value):
    """
    Creates a default entry with default value inserted.
    :param master: the parent of the tk object.
    :param default_value: default value to begin with.
    :return: an Entry object.
    """
    entry = Entry(
        master=master,
        font=fonts.regular,
        width=7,
        bg=palette.btn_bg,
        fg=palette.btn_fg,
        justify='center'
    )
    entry.insert(0, default_value)
    return entry


class App(Tk):
    """
    This class defines the behaviour of the app and its window.
    """

    def __init__(self):
        """
        App constructor - initializes the windows and its contents.
        :return: App object.
        """

        # Inherit Tkinter class and configure it.
        super().__init__()
        self.geometry('1100x830')
        self.minsize(1100, 830)
        self.maxsize(1100, 830)
        self.configure(background=palette.bg, highlightcolor=palette.fg)
        self.title('Corona Waves')
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.destroy()
                exit(0)
        self.protocol("WM_DELETE_WINDOW", on_closing)

        # Create a frame for a cellular automata, and instantiate and automata.
        self.frame = Canvas(
            bg=palette.canvas_bg,
            bd=0,
            highlightbackground=palette.canvas_outline,
            width=800,
            height=800)
        self.frame.place(relx=0.26, rely=0.025)
        self.automata = Automata(self)

        # Create configurations section with labels, entries and buttons.
        self.configuration = LabelFrame(
            master=self,
            bg=palette.bg,
            fg=palette.fg,
            text='Configuration',
            font=fonts.regular
        )
        self.configuration.place(relx=0.01, rely=0.015, width=265)

        Label(
            master=self.configuration,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Number of creatures:'
        ).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.n_creature = createEntry(self.configuration, '4000')
        self.n_creature.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.configuration,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Infection percentage:'
        ).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.p_infected = createEntry(self.configuration, '0.5')
        self.p_infected.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.configuration,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Fast movers percentage:'
        ).grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.p_quick = createEntry(self.configuration, '0.5')
        self.p_quick.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.configuration,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Days for healing:'
        ).grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.healing_time = createEntry(self.configuration, '50')
        self.healing_time.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.configuration,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='High probability:'
        ).grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.high_probability = createEntry(self.configuration, '0.7')
        self.high_probability.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.configuration,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Low probability:'
        ).grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.low_probability = createEntry(self.configuration, '0.3')
        self.low_probability.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.configuration,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Threshold:'
        ).grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.threshold = createEntry(self.configuration, '0.5')
        self.threshold.grid(row=6, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.configuration,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Generation limit (Optional):'
        ).grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.gen_limit = createEntry(self.configuration, '')
        self.gen_limit.grid(row=7, column=1, padx=5, pady=5, sticky='w')

        self.pause_btn = Button(
            master=self,
            width=12,
            bg=palette.btn_bg,
            fg=palette.btn_fg,
            relief='groove',
            font=fonts.bold,
            text='\u23F8 Pause',
            command=self.pause_btn_action
        )
        self.pause_btn.place(relx=0.01, rely=0.745, width=125, height=40)

        self.stop_btn = Button(
            master=self,
            width=12,
            bg=palette.btn_bg,
            fg=palette.btn_fg,
            relief='groove',
            font=fonts.bold,
            text='\u23F9 Stop',
            command=self.stop_btn_action
        )
        self.stop_btn.place(relx=0.137, rely=0.745, width=125, height=40)

        self.run_btn = Button(
            master=self,
            width=27,
            bg=palette.btn_bg,
            fg=palette.btn_fg,
            relief='groove',
            font=fonts.bold,
            text='\u23F5 Start   ',
            command=self.run_btn_action
        )
        self.run_btn.place(relx=0.01, rely=0.745, width=265, height=40)

        # Create information section with labels and entries.
        self.information = LabelFrame(
            master=self,
            bg=palette.bg,
            fg=palette.fg,
            text='Information',
            font=fonts.regular
        )
        self.information.place(relx=0.01, rely=0.38, width=265)

        Label(
            master=self.information,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Generation:'
        ).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.generation = createEntry(self.information, 'n/a')
        self.generation.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.information,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Infected creatures:'
        ).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.n_infected = createEntry(self.information, 'n/a')
        self.n_infected.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.information,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Distribution of infection:'
        ).grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.distribution = createEntry(self.information, 'n/a')
        self.distribution.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        Label(
            master=self.information,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text='Infection to threshold ratio:'
        ).grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.capacity = createEntry(self.information, 'n/a')
        self.capacity.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        # Create Legend section.
        self.legend = LabelFrame(
            master=self,
            bg=palette.bg,
            fg=palette.fg,
            text='Legend',
            font=fonts.regular
        )
        self.legend.place(relx=0.01, rely=0.585, width=265)

        Label(
            master=self.legend,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text=' \u2022  White - healthy.'
        ).grid(row=0, column=0, padx=5, pady=0, sticky='w')

        Label(
            master=self.legend,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text=' \u2022  Cyan - healthy and quick.'
        ).grid(row=1, column=0, padx=5, pady=0, sticky='w')

        Label(
            master=self.legend,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text=' \u2022  Orange - infected.'
        ).grid(row=2, column=0, padx=5, pady=0, sticky='w')

        Label(
            master=self.legend,
            font=fonts.regular,
            bg=palette.bg,
            fg=palette.fg,
            text=' \u2022  Red - infected and quick.'
        ).grid(row=3, column=0, padx=5, pady=0, sticky='w')

        # Credit.
        Label(
            master=self,
            font=fonts.credit,
            bg=palette.bg,
            fg=palette.fg,
            text='\u00A9 Created by Shlomi Ben-Shushan and Itamar Laredo'
        ).place(relx=0.006, rely=0.97)

    def get_input(self):
        """
        Get inputs from the app's entries and validates them. If at least one of
        the inputs are invalid, raise a descriptive error message. Otherwise,
        return validated input.
        :return: simulation's input -- experiment's parameters.
        """

        error_messages = []
        N, D, X, R, PH, PL, T = 0, 0, 0, 0, 0, 0, 0

        try:
            N = int(self.n_creature.get().strip())
            if N <= 0 or N > 40000:
                raise ValueError
        except ValueError:
            msg = 'Number of creatures must be an int between 1 and 40000.'
            error_messages.append(msg)

        try:
            D = float(self.p_infected.get().strip())
            if D < 0 or D > 1:
                raise ValueError
        except ValueError:
            msg = 'Infection percentage must be a float between 0 and 1.'
            error_messages.append(msg)

        try:
            X = int(self.healing_time.get().strip())
            if X <= 0:
                raise ValueError
        except ValueError:
            msg = 'Days for healing must be a positive integer.'
            error_messages.append(msg)

        try:
            R = float(self.p_quick.get().strip())
            if R < 0 or R > 1:
                raise ValueError
        except ValueError:
            msg = 'Fast movers percentage must be a float between 0 and 1.'
            error_messages.append(msg)

        try:
            PH = float(self.high_probability.get().strip())
            if PH < 0 or PH > 1:
                raise ValueError
        except ValueError:
            msg = 'High probability must be a float between 0 and 1.'
            error_messages.append(msg)

        try:
            PL = float(self.low_probability.get().strip())
            if PL < 0 or PL > 1:
                raise ValueError
        except ValueError:
            msg = 'Low probability must be a float between 0 and 1.'
            error_messages.append(msg)

        try:
            T = float(self.threshold.get().strip())
            if T < 0 or T > 1:
                raise ValueError
        except ValueError:
            msg = 'Threshold must be a float between 0 and 1.'
            error_messages.append(msg)

        L = self.gen_limit.get().strip()
        if L == '':
            L = 0
        else:
            try:
                L = int(L)
                if L <= 0:
                    raise ValueError
            except ValueError:
                msg = 'Generation limit must be a positive integer (or empty).'
                error_messages.append(msg)

        if len(error_messages) == 0:
            return N, D, X, R, PH, PL, T, L
        messagebox.showerror('Input Error', '\n'.join(error_messages))
        return None

    def run_btn_action(self):
        """
        Defines the action to be taken when user clicks the "Start"/"Resume"
        button. Note that those are the same button with changing label.
        :return: None.
        """
        if self.automata.state.is_stopped:
            params = self.get_input()
            if params:
                N, D, X, R, PH, PL, T, L = params
                self.run_btn.place_forget()
                self.automata.set(N, D, X, R, PH, PL, T, L)
                self.automata.run()
        elif self.automata.state.is_paused:
            self.run_btn.place_forget()
            self.automata.run()

    def pause_btn_action(self):
        """
        Defines the action to be taken when user clicks the "Pause" button.
        :return: None.
        """
        self.run_btn.place(relx=0.01, rely=0.745, width=265, height=40)
        self.run_btn.configure(text='\u23F5 Resume  ', font=fonts.bold)
        self.automata.pause()

    def stop_btn_action(self):
        """
        Defines the action to be taken when user click the "Stop" button.
        :return: None.
        """
        self.run_btn.place(relx=0.01, rely=0.745, width=265, height=40)
        self.run_btn.configure(text='\u23F5 Start   ', font=fonts.bold)
        self.automata.stop()
