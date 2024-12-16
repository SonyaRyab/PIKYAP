from project.main import g3, gen_mtm, DataTable, DataColumn, TableColumns


def test_g3():
    tables = [DataTable(1, "D"),
              DataTable(2, "C"),
              DataTable(3, "A"),
              DataTable(4, "B")]

    columns = [DataColumn(11, "1", 2, 1),
               DataColumn(12, "2", 1, 1),
               DataColumn(21, "3", 3, 2),
               DataColumn(22, "4", 2, 2),
               DataColumn(31, "5", 10, 3),
               DataColumn(32, "6", 11, 3),
               DataColumn(41, "7", 20, 4),
               DataColumn(42, "8", 0, 4)
               ]
    tabCol = [
        TableColumns(11, 1),
        TableColumns(12, 1),
        TableColumns(12, 2),
        TableColumns(21, 2),
        TableColumns(22, 2),
        TableColumns(31, 3),
        TableColumns(32, 3),
        TableColumns(41, 4),
        TableColumns(42, 4)
    ]

    a = g3(gen_mtm(columns, tables, tabCol))
    assert a == [('5', 'A'), ('6', 'A'), ('7', 'B'), ('8', 'B'), ('2', 'C'), ('3', 'C'), ('4', 'C'), ('1', 'D'),
                 ('2', 'D')]
