from project.main import g2, gen_otm, DataTable, DataColumn


def test_g2():
    tables = [DataTable(1, "Se"),
              DataTable(2, "Sx"),
              DataTable(3, "S"),
              DataTable(4, "A")]

    columns = [DataColumn(11, "A", 2, 1),
               DataColumn(12, "B", 1, 1),
               DataColumn(21, "B", 3, 2),
               DataColumn(22, "C", 2, 2),
               DataColumn(31, "C", 10, 3),
               DataColumn(32, "D", 11, 3),
               DataColumn(41, "E", 20, 4),
               DataColumn(42, "F", 0, 4)
               ]

    a = g2(gen_otm(columns, tables))
    assert a == [('A', 20), ('S', 11), ('Sx', 3), ('Se', 2)]
