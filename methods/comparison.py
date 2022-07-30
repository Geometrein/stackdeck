from methods.search import search_by_company_name


def stack_similarity(first_card: str, second_card: str) -> dict:
    firs_company = search_by_company_name(company_name=first_card)
    second_company = search_by_company_name(company_name=second_card)
    result = set(firs_company['stack']).intersection(set(second_company['stack']))
    result = {
        'similarity': result,
    }
    return result


def stack_difference(first_card: str, second_card: str) -> dict:
    firs_company = search_by_company_name(company_name=first_card)
    second_company = search_by_company_name(company_name=second_card)
    result = set(firs_company['stack']).difference(set(second_company['stack']))
    result = {
        'difference': result,
    }
    return result


def stack_symmetric_difference(first_card: str, second_card: str) -> dict:
    firs_company = search_by_company_name(company_name=first_card)
    second_company = search_by_company_name(company_name=second_card)
    result = set(firs_company['stack']).symmetric_difference(set(second_company['stack']))
    result = {
        'symmetric_difference': result,
    }
    return result
