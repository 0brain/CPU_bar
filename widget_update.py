class Configure_widgets:

    def configure_cpu_bar(self):

        r = self.cpu.cpu_percent_return() # each processor flow loading
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core {i+1} usage: {r[i]}%')
            self.list_pbar[i].configure(value=r[i])

        r2 = self.cpu.ram_usage()
        self.ram_lab.configure(text=f'RAM usage: {r2[2]}%, used {round(r2[3] / 1048576)} Mb,\
                    \n available: {round(r2[1] / 1048576)} Mb')
        self.ram_bar.configure(value=r2[2])

        self.after(1000, self.configure_cpu_bar)