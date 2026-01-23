from db_init import supa_db, supa_table


def create_rows(rowData):
    create_resp = supa_db.table(supa_table).insert(rowData).execute()
    print("Create Response:", create_resp)


def upsert_rows(rowData):
    upsert_resp = supa_db.table(supa_table).upsert(rowData).execute()
    print("Upsert Response:", upsert_resp)


def read_rows():
    read_resp = supa_db.table(supa_table).select("*").limit(100).execute()
    print("Read Response:", read_resp)


def update_rows(newData, queryFilter):
    if len(queryFilter) < 1:
        print("Update operation requires a valid 'id' value in queryFilter")
        return
    elif len(queryFilter) == 1:
        update_single_resp = (
            supa_db.table(supa_table).update(newData).eq("id", queryFilter[0]).execute()
        )
        print("Update Single Response:", update_single_resp)
    elif len(queryFilter) > 1:
        update_multiple_resp = (
            supa_db.table(supa_table).delete().in_("id", queryFilter).execute()
        )
        print("Update Multiple Response:", update_multiple_resp)


def delete_rows(queryFilter):
    if len(queryFilter) < 1:
        print("Delete operation requires a valid 'id' value in queryFilter")
        return
    elif len(queryFilter) == 1:
        delete_single_resp = (
            supa_db.table(supa_table).delete().eq("id", queryFilter[0]).execute()
        )
        print("Delete Single Response:", delete_single_resp)
    elif len(queryFilter) > 1:
        delete_mutiple_resp = (
            supa_db.table(supa_table).delete().in_("id", queryFilter).execute()
        )
        print("Delete Multiple Response:", delete_mutiple_resp)


if __name__ == "__main__":
    create_rows(
        [
            {"ip_address": "check 1"},
            {"ip_address": "check 2"},
            {"ip_address": "check 3"},
        ]
    )
    upsert_rows(
        [{"id": 4, "ip_address": "check 4"}, {"id": 5, "ip_address": "check 5"}]
    )
    read_rows()
    update_rows([{"ip_address": "checking single update"}], [3])
    update_rows([{"ip_address": "checking multiple update"}], [4, 5])
    read_rows()
    delete_rows([3])
    delete_rows([4, 5])
    read_rows()
