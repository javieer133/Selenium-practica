# encoding: utf-8

import os
import subprocess


class DictBuilderBase(dict):
    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default


class QuestionType(DictBuilderBase):
    pass


class ReportType(DictBuilderBase):
    pass


class ActionsType(DictBuilderBase):
    pass


class EditType(DictBuilderBase):
    pass


class DeleteType(DictBuilderBase):
    pass


class OptionsType(DictBuilderBase):
    pass


class TestingMachineQServus(object):

    displayer = []
    all_tests = []
    project_folder = os.path.dirname(os.path.realpath(__file__))

    folders_questions_type = [
        "Texto", "Fecha", "Foto", "Selección", "Checklist",
        "Términos_y_condiciones", "Escala_de_caras",
        "Escala_de_estrellas", "Escala_de_números",
        "Matrices", "MaxDiff", "Mixta"
    ]

    folders_report_type = [
        "Campañas",
        "Sensores",
        "Pautas",
        "Avanzados",
        "Historial_del_cliente"
    ]

    folders_actions_type = [
        "Obtener_opinion/Felicitaciones",
        "Obtener_opinion/Sugerencia",
        "Obtener_opinion/Reclamo",
        "Enviar_notificacion/Satisfacción",
        "Enviar_notificacion/Insatisfacción",
        "Enviar_notificacion/Personalizada",
        "Enviar_informacion",
        "Ejecutar_proceso"
    ]

    folders_edit_type = [
        "Pautas/Editar_Pautas",
        "Sensores/Editar_Sensores",
        "Campañas/Editar_Campañas",
    ]

    folders_delete_type = [
        "Pautas/Eliminar_Pautas",
        "Sensores/Eliminar_Sensores",
        "Campañas/Eliminar_Campañas"
    ]

    folders_options_type = [
        "Configurar_perfil",
        "Ayuda"
    ]

    # Functions
    def __init__(self):

        # Loads Dictionaries
        self.options_type_dict = OptionsType()
        self.options_type_dict = self.dictbuilder(
            dictionary=self.options_type_dict,
            printlist=self.folders_options_type
        )

        self.delete_type_dict = DeleteType()
        self.delete_type_dict = self.dictbuilder(
            dictionary=self.delete_type_dict,
            printlist=self.folders_delete_type
        )

        self.edit_type_dict = EditType()
        self.edit_type_dict = self.dictbuilder(
            dictionary=self.edit_type_dict,
            printlist=self.folders_edit_type
        )

        self.actions_type_dict = ActionsType()
        self.actions_type_dict = self.dictbuilder(
            dictionary=self.actions_type_dict,
            printlist=self.folders_actions_type
        )

        self.report_type_dict = ReportType()
        self.report_type_dict = self.dictbuilder(
            dictionary=self.report_type_dict,
            printlist=self.folders_report_type
        )

        self.question_type_dict = QuestionType()
        self.question_type_dict = self.dictbuilder(
            dictionary=self.question_type_dict,
            printlist=self.folders_questions_type
        )

    def welcome_menu(self):

        current_path = os.path.dirname(os.path.realpath(__file__))
        doc_path = current_path + "/Pruebas_Selenium/Archivos/VariableParaEvitarBorrar.txt"
        print(doc_path)
        file = open (doc_path,"r")
        skip = file.read()
        file.close()


        welcome_menu = [
            "Bienvenido a la QServus TM",
            "¿Que desea hacer?:", 
            "1. Escuchar / Analizar / Actuar",
            "2. Eliminar", 
            "3. Opciones", 
            "4. Mostrar lista de tests",
            "5. Ejecutar lista de tests",
            "6. Limpiar lista de tests",
            "7. Limpiar Qservus (Borrar pautas, campañas, sensores)",
            "8. Cambiar prefijo (Prefijo actual --> '{}' )".format(skip),
            "9. Salir", "\n"
        ]

        print("\n".join(welcome_menu))
        try:
            welcome_choice = int(input())

        except ValueError:
            self.welcome_menu()

        else:
            if welcome_choice == 1:
                self.firstchoice_menu()

            elif welcome_choice == 2:
                self.delete_menu()

            elif welcome_choice == 3:
                self.options_menu()

            elif welcome_choice == 4:
                self.list_displayer(self.displayer)

            elif welcome_choice == 5:
                self.executioner(self.all_tests)

            elif welcome_choice == 6:
                self.clear_list()
            elif welcome_choice == 7:
                self.clear_qservus()

            elif welcome_choice == 8:
                self.change_prefix()

            elif welcome_choice == 9:
                exit()

            else:
                self.welcome_menu()

    def firstchoice_menu(self):

        firstchoice_menu = [
            "\n", "- Escuchar: ¿Que desea crear?\n",
            "1. Pauta\n", "2. Sensor\n", "3. Campaña\n",
            "\n", "- Analizar: ¿Generar R/I?\n", "4. Reportes\n",
            "5. Indicadores\n", "\n", "- Actuar: Generar Acciones\n",
            "6. Acciones\n", "\n", "- Editar:\n",
            "7. Editar pauta, sensor o campaña\n", "\n",
            "8. Cancelar: Retroceder\n", "\n",
        ]

        print("".join(firstchoice_menu))

        try:
            first_choice = int(input())

        except ValueError:
            self.firstchoice_menu()

        else:
            if first_choice == 1:
                self.template_menu()

            elif first_choice == 2:
                self.sensor_menu()

            elif first_choice == 3:
                self.campaign_menu()

            elif first_choice == 4:
                self.report_menu()

            elif first_choice == 5:
                self.indicators_menu()

            elif first_choice == 6:
                self.actions_menu()

            elif first_choice == 7:
                self.edit_menu()

            elif first_choice == 8:
                self.welcome_menu()

            else:
                self.firstchoice_menu()

    def template_menu(self):

        template_menu = [
            "\n", "Crear Pauta:\n", "Tipos de pregunta:\n",
            "1. Texto\n", "2. Fecha\n", "3. Foto\n", "4. Selección\n",
            "5. Checklist\n", "6. Términos y condiciones\n",
            "7. Escala de caras\n", "8. Escala de estrellas\n",
            "9. Escala de números\n", "10. Matrices\n", "11. MaxDiff\n",
            "12. Mixta\n", "-\n", "13. Cancelar: Retroceder\n", "\n"
        ]

        print("".join(template_menu))

        try:
            question_type = int(input())

        except ValueError:
            self.template_menu()

        else:
            OPTIONS = list(range(1, 13))

            if question_type == 13:
                self.firstchoice_menu()

            elif question_type in OPTIONS:
                path = self.pathbuilder(question_type, self.question_type_dict)
                self.tailer(path, self.all_tests)

            else:
                self.template_menu()

    def sensor_menu(self):

        sensor_menu = [
            "\n", "1. Crear Sensor\n", "2. Cancelar: Retroceder\n", "\n"
        ]

        print("".join(sensor_menu))

        try:
            sensor_choice = int(input())
        except ValueError:
            self.sensor_menu()

        else:
            if sensor_choice == 1:
                path = "{}/Pruebas_Selenium/Sensores/Crear_Sensores/".\
                    format(self.project_folder)
                self.tailer(path, self.all_tests)

            elif sensor_choice == 2:
                self.firstchoice_menu()

            else:
                self.sensor_menu()

    def campaign_menu(self):

        campaign_menu = [
            "\n", "1. Crear Campaña:\n", "2. Cancelar: Retroceder\n", "\n"
        ]

        print("".join(campaign_menu))

        try:
            campaign_choice = int(input())

        except ValueError:
            self.campaign_menu()

        if campaign_choice == 1:
            path = "{}/Pruebas_Selenium/Campañas/Crear_Campañas/".\
                format(self.project_folder)
            self.tailer(path, self.all_tests)

        elif campaign_choice == 2:
            self.firstchoice_menu()

        else:
            self.campaign_menu()

    def report_menu(self):

        report_menu = [
            "\n", "Generar Reporte:\n", "1. Reporte campaña\n",
            "2. Reporte sensor\n", "3. Reporte pauta\n",
            "4. Reporte avanzado\n", "5. Reporte historial del cliente\n",
            "-\n", "6. Cancelar: Retroceder\n", "\n"
        ]

        print("".join(report_menu))

        try:
            report_choice = int(input())

        except ValueError:
            self.report_menu()

        else:
            OPTIONS = list(range(1, 6))

            if report_choice == 6:
                self.firstchoice_menu()

            elif report_choice in OPTIONS:
                path = self.pathbuilder(report_choice, self.report_type_dict)
                self.tailer(path, self.all_tests)

            else:
                self.report_menu()

    def indicators_menu(self):

        indicators_menu = [
            "\n", "1. Generar Indicadores:\n", "2. Cancelar: Retroceder\n",
            "\n"
        ]

        print("".join(indicators_menu))

        try:
            indicators_choice = int(input())

        except ValueError:
            self.indicators_menu()

        else:
            if indicators_choice == 1:
                path = "{}/Pruebas_Selenium/Indicadores".\
                    format(self.project_folder)
                self.tailer(path, self.all_tests)

            elif indicators_choice == 2:
                self.firstchoice_menu()

            else:
                self.indicators_menu()

    def actions_menu(self):

        actions_menu = [
            "\n", "Generar Acciones:\n", "- Obtener opinión:\n",
            "     1. Felicitaciones\n", "     2. Sugerencia\n",
            "     3. Reclamo\n", "\n", "- Enviar notificación\n",
            "     4. Satisfacción\n", "     5. Insatisfacción\n",
            "     6. Personalizada\n", "\n", "-    7. Enviar información\n",
            "\n", "-    8. Ejecutar proceso  \n",
            "                                  \n",
            "-    9. Cancelar: Retroceder\n", "\n"
        ]

        print("".join(actions_menu))
        try:
            actions_choice = int(input())

        except ValueError:
            self.actions_menu()

        else:
            OPTIONS = list(range(1, 9))

            if actions_choice == 9:
                self.firstchoice_menu()

            elif actions_choice in OPTIONS:
                path = self.pathbuilder(actions_choice, self.actions_type_dict)
                self.tailer(path, self.all_tests)

            else:
                self.actions_menu()

    def edit_menu(self):

        edit_menu = [
            "\n", "Editar:\n", "1. Pauta\n", "2. Sensor\n",
            "3. Campaña\n", "-\n", "4. Cancelar: Retroceder\n", "\n"
        ]

        print("".join(edit_menu))

        try:
            edit_choice = int(input())

        except ValueError:
            self.edit_menu()

        else:
            OPTIONS = list(range(1, 4))

            if edit_choice == 4:
                self.firstchoice_menu()

            elif edit_choice in OPTIONS:
                path = self.pathbuilder(edit_choice, self.edit_type_dict)
                self.tailer(path, self.all_tests)

            else:
                self.edit_menu()

    def delete_menu(self):

        delete_menu = [
            "\n", "Eliminar:\n", "1. Pauta\n", "2. Sensor\n",
            "3. Campaña\n", "-\n", "4. Cancelar: Retroceder\n", "\n"
        ]

        print("".join(delete_menu))

        try:
            delete_choice = int(input())

        except ValueError:
            self.delete_menu()

        else:
            OPTIONS = list(range(1, 4))

            if delete_choice == 4:
                self.welcome_menu()

            elif delete_choice in OPTIONS:
                path = self.pathbuilder(delete_choice, self.delete_type_dict)
                self.tailer(path, self.all_tests)

            else:
                self.delete_menu()

    def options_menu(self):

        options_menu = [
            "\n", "Opciones:\n", "1. Configurar perfil\n",
            "2. Ayuda\n", "-\n", "3. Cancelar: Retroceder\n", "\n"
        ]

        print("".join(options_menu))

        try:
            options_choice = int(input())

        except ValueError:
            self.options_menu()

        else:
            OPTIONS = list(range(1, 3))

            if options_choice in OPTIONS:
                path = self.pathbuilder(options_choice, self.options_type_dict)
                self.tailer(path, self.all_tests)

            elif options_choice == 3:
                self.welcome_menu()

            else:
                self.options_menu()

    def pathbuilder(self, choice, dictionary):

        for key, value in dictionary.items():
            if key == choice:
                format_path = "{}/Pruebas_Selenium/{}".\
                    format(self.project_folder, str(value))

                return format_path

    def tailer(self, path, all_tests):

        """ show content folder """
        test_list = []  # test_list saves a list of the files in path
        enum = 1
        print (path)
        for testcase in os.listdir(path):
            # prints a numbered list of the files in path
            print(str(enum) + ". " + str(testcase))
            # adds test to the path building for execution and display
            test_list.append(testcase)
            enum += 1

        try:
            test_choice = int(input())

        except ValueError:
            self.template_menu()

        try:
            path = path + "/" + test_list[test_choice - 1]

        except (ValueError, IndexError):
            self.template_menu()

        list_or_exec_printlist = [
            "Añadir Prueba o ejecutar:",
            "1. Añadir a la lista",
            "2. Ejecutar Prueba",
            "3. Ejecutar Prueba indefinidamente",
            "4. Cancelar: Retroceder", ""
        ]

        try:
            list_or_exec = int(input("\n".join(list_or_exec_printlist)))

        except ValueError:
            self.template_menu()

        else:
            if list_or_exec == 1:
                all_tests.append(['python', path])
                self.displayer.append(test_list[test_choice - 1])

            elif list_or_exec == 2:
                print("Ejecutando " + test_list[test_choice - 1] + "...")
                subprocess.call(['python', path])  # Ejecuta el test_choice
            elif list_or_exec == 3:

                repetitions = int(input("Indicar numero de repeticiones"))
                for i in range(1,repetitions+1):
                    try:
                        print("Ejecutando " + test_list[test_choice - 1] + " ({})...".format(i))
                        subprocess.call(['python', path])
                    except:
                        print("Ya no se puede seguir ejecutando el test...")
                        break

            else:
                self.template_menu()

        return all_tests

    def list_displayer(self, list_displayer):

        enum = 1
        print("\n")
        for test in list_displayer:
            print(str(enum) + ". " + test)
            enum += 1

    def executioner(self, all_the_tests):

        print("Ejecutando lista de tests...")
        for lista in all_the_tests:
            subprocess.call(lista)

    def clear_list(self):
        print("Limpiando lista de tests...")
        self.all_tests = []
        self.displayer = []


    def clear_qservus(self):
        print("Comenzando limpieza de encuestas...")
        print("1--->   Limpiando sensores...")
        subprocess.call(['python',"{}/Pruebas_Selenium/Sensores/Eliminar_Sensores/Finalizar-EliminarTodosSensores.py".format(self.project_folder)])
        print("        Limpieza de sensores finalizada")
        print("2--->   Eliminando campañas en creacion...")
        subprocess.call(['python',"{}/Pruebas_Selenium/Campañas/Eliminar_Campañas/EliminarCampañasEnCreacion.py".format(self.project_folder)])
        print("        Eliminacion de campañas en creacion finalizada")
        print("3--->   Finalizando campañas en ejecucion...")
        subprocess.call(['python',"{}/Pruebas_Selenium/Campañas/Eliminar_Campañas/FinalizarCampañasEnEjecucion.py".format(self.project_folder)])
        print("        Finalizacion de campañas en ejecucion finalizada")
        print("4--->   Eliminando campañas finalizadas...")
        subprocess.call(['python',"{}/Pruebas_Selenium/Campañas/Eliminar_Campañas/EliminarCampañasFinalizadas.py".format(self.project_folder)])
        print("        Eliminacion de campañas finalizadas, finalizada")
        print("5--->   Eliminando todas las pautas...")
        subprocess.call(['python',"{}/Pruebas_Selenium/Pautas/Eliminar_Pautas/EliminarTodasLasPautas.py".format(self.project_folder)])
        print("        Eliminacion de todas las pautas, finalizada")


    def change_prefix(self):
                                
        current_path = os.path.dirname(os.path.realpath(__file__))
        doc_path = current_path + "/Pruebas_Selenium/Archivos/VariableParaEvitarBorrar.txt"
        file = open (doc_path,"w")
        changing = input(" Cual es el nuevo prefijo (?) :   " )
        file.write(changing)
        file.close()
        print(" Prefijo exitosamente cambiado a {} !".format(changing))


    def dictbuilder(self, **options):

        dictionary = options.get('dictionary')
        printlist = options.get('printlist')

        if isinstance(dictionary, QuestionType):
            for index, questions_type in enumerate(printlist):
                dictionary.update({
                    index + 1: "Pautas/Crear_Pautas/{}/".format(questions_type)
                })

            return dictionary

        elif isinstance(dictionary, ReportType):
            for index, reports_type in enumerate(printlist):
                dictionary.update({
                    index + 1: "Reportes/{}/".format(reports_type)
                })

            return dictionary

        elif isinstance(dictionary, ActionsType):
            for index, actions_type in enumerate(printlist):
                dictionary.update({
                    index + 1: "Acciones/{}/".format(actions_type)
                })

            return dictionary

        elif isinstance(dictionary, EditType):
            for index, edit_type in enumerate(printlist):
                dictionary.update({
                    index + 1: "{}/".format(edit_type)
                })

            return dictionary

        elif isinstance(dictionary, DeleteType):
            for index, delete_type in enumerate(printlist):
                dictionary.update({
                    index + 1: "{}/".format(delete_type)
                })

            return dictionary

        elif isinstance(dictionary, OptionsType):
            for index, edit_type in enumerate(printlist):
                dictionary.update({
                    index + 1: "Opciones/{}/".format(edit_type)
                })

            return dictionary

        else:
            return {}


# Code
if __name__ == '__main__':
    testing = TestingMachineQServus()

    while True:
        testing.welcome_menu()
