#from ..dependencies import get_token_header
from ..models import Branch
from ..database import get_session

from fastapi import APIRouter, Depends, HTTPException

from http import HTTPStatus

from typing import Annotated

from sqlalchemy.orm import Session

from ..schemas import(
    BranchPublic,
    ListBranchPublic
)

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/branches",
    tags=["branches"],
    #dependencies=[Depends(get_token_header)], Adicionar futuramente quando estiver implementado funcional
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    status_code=HTTPStatus.OK,
    response_model=ListBranchPublic
)
def read_branches(
    session:SessionDep
):
    branches = Branch.get_all(session)
    
    if len(branches) == 0:
        raise HTTPException(status_code=404, detail="Table is empty")
    return {"branches": branches}


@router.get(
    "/{branch_id}",
    status_code=HTTPStatus.OK,
    response_model=BranchPublic
)
def read_branch(branch_id:str, session: SessionDep):
    branch = Branch.get_by_id(branch_id, session)
    
    if branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch

