
  def test_un_archivo_del_2012_no_es_del_milenio_pasado(self):
    archivo = {"ruta":"", "creacion":"01/01/2012"}
    self.assertIs(es_del_milenio_pasado(archivo), False, "debe devolver False")
  
  def test_un_archivo_de_2000_no_es_del_milenio_pasado(self):
    archivo = {"ruta":"", "creacion":"01/01/2000"}
    self.assertIs(es_del_milenio_pasado(archivo), False, "debe devolver False")
  
  def test_un_archivo_de_1999_es_del_milenio_pasado(self):
    archivo = {"ruta":"", "creacion":"23/09/1994"}
    self.assertIs(es_del_milenio_pasado(archivo),  True, "debe devolver True")
  
  def test_un_archivo_de_1994_es_del_milenio_pasado(self):
    archivo = {"ruta":"", "creacion":"23/09/1994"}
    self.assertIs(es_del_milenio_pasado(archivo),  True, "debe devolver True")