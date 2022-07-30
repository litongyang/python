from db.db_connect import youke



def df_yk():
    sql = """
    select distinct CAST(AES_DECRYPT(from_base64(a.mobile),sign) as char(256)) dest_number
    from `uk-customer`.customer_info a
    inner join
    (select mobile,min(create_time) create_time from `uk-customer`.customer_info GROUP BY mobile  ) b
    on a.mobile = b.mobile AND a.create_time = b.create_time
    where a.name is not null
    """
    df_yk = youke(sql)
    return df_yk

