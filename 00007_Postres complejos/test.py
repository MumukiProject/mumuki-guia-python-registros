
  def setUp(self):
    self.flan_casero = { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tiempo_de_coccion": 50 }
    self.cheesecake = { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }
    self.lemon_pie = { "ingredientes": ["jugo de limón", "almidón de maíz", "leche", "huevos"], "tiempo_de_coccion": 65 }
    
  def test_el_flan_casero_es_mas_dificil_de_cocinar_que_el_cheesecake_al_derecho(self):
    self.assertEqual(mas_dificil_de_cocinar(self.flan_casero, self.cheesecake), self.flan_casero, "mas_dificil_de_cocinar(flan_casero, cheesecake) debe devolver flan_casero")

  def test_el_flan_casero_es_mas_dificil_de_cocinar_que_el_cheesecake_al_reves(self):
    self.assertEqual(mas_dificil_de_cocinar(self.cheesecake, self.flan_casero), self.flan_casero, "mas_dificil_de_cocinar(cheesecake, flan_casero) debe devolver flan_casero")

  def test_el_lemon_pie_es_mas_dificil_de_cocinar_que_el_cheesecake_al_derecho(self):
    self.assertEqual(mas_dificil_de_cocinar(self.cheesecake, self.lemon_pie), self.lemon_pie, "mas_dificil_de_cocinar(cheescake, lemon_pie) debe devolver lemon_pie")

  def test_el_lemon_pie_es_mas_dificil_de_cocinar_que_el_cheesecake_al_reves(self):
    self.assertEqual(mas_dificil_de_cocinar(self.lemon_pie, self.cheescake), self.lemon_pie, "mas_dificil_de_cocinar(lemon_pie, cheescake) debe devolver lemon_pie")

  def test_si_dos_postres_son_igual_de_dificiles_de_cocinar_devuelve_cualquiera_de_los_dos(self):
    mas_dificil = mas_dificil_de_cocinar(self.flan_casero, self.lemon_pie)
    self.assertTrue(mas_dificil == self.flan_casero or mas_dificil == self.lemon_pie)