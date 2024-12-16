from project.main import g1, gen_otm, DataTable, DataColumn


def test_g1():
    tables = [DataTable(1, "Se"),
              DataTable(2, "Sx"),
              DataTable(3, "S"),
              DataTable(4, "A")]

    columns = [DataColumn(11, "A", 1024, 1),
               DataColumn(12, "B", 1024, 1),
               DataColumn(21, "B", 1024, 2),
               DataColumn(31, "C", 1024, 3),
               DataColumn(41, "D", 1024, 4)
               ]
    a1, a2 = g1(gen_otm(columns, tables))
    assert sorted(a1) == sorted(["Se", "Sx", "S"]) and sorted(a2) == sorted(["A", "B", "C"])
