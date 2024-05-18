import collections

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._btn_connected.disabled = False
        self._view._btn_cerca_vicini.disabled = False
        self._view._txt_result.controls.clear()
        anno = self._view._txtAnno.value
        if anno == "" or int(anno) <= 1816 or int(anno) >= 2016 :
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è corretto!!", color="red"))
            self._view._txtAnno.value = ""
            self._view.update_page()
            return
        self._model.buildGraph(anno)
        dizionario = self._model.getVicini(anno)
        dizionario = collections.OrderedDict(sorted(dizionario.items()))
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato correttamente"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo creato ha {self._model.getConnessi()} componenti connesse"))
        for key, value in dizionario.items():
            self._view._txt_result.controls.append(ft.Text(f"{key.StateNme} --- {value} vicini"))
        self._view.update_page()

    def handleConnected(self, e):
        self._view._txt_result.controls.clear()
        nodoStarter = self._view._ddNearby.value
        if nodoStarter == "":
            self._view._txt_result.controls.append(ft.Text("Non è stata selezionata nessuna scelta!!", color="red"))
            self._view.update_page()
            return
        nodiConnessi = self._model.getNodiConnessi(nodoStarter)
        if len(nodiConnessi) == 0:
            self._view._txt_result.controls.append(ft.Text(f"Lo stato cercato non è connesso a nulla"))
            self._view.update_page()
            return
        for nodi in nodiConnessi:
            self._view._txt_result.controls.append(ft.Text(f"Lo stato cercato è connesso a: {nodi.StateNme}"))
        self._view.update_page()

    def handleCercaVicini(self, e):
        self._view._txt_result.controls.clear()
        nodoStarter = self._view._ddNearby.value
        vicini = self._model.getConfinanti(nodoStarter)
        if nodoStarter == "":
            self._view._txt_result.controls.append(ft.Text("Non è stata selezionata nessuna scelta!!", color="red"))
            self._view.update_page()
            return
        if len(vicini) == 0:
            self._view._txt_result.controls.append(ft.Text(f"Lo stato cercato non è connesso a nulla"))
            self._view.update_page()
            return
        for nodi in vicini:
            self._view._txt_result.controls.append(ft.Text(f"Lo stato cercato è confinante con: {nodi.StateNme}"))
        self._view.update_page()

    def riempi_dropdown(self):
        nodi = self._model._stati
        for n in nodi:
            self._view._ddNearby.options.append(ft.dropdown.Option(key=n.CCode, text=n.StateNme))

