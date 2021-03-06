from operator import and_

from flask import jsonify

from database import db_transaction
from database.entities.account import Account
from database.entities.statement import Statement
from models.web.statement_response import StatementSchema


class StatementService:
    def get(self, accnum):
        try:
            with db_transaction() as txn:
                statement_lines = txn.query(Statement).join(Account).filter(
                    and_(
                        Statement.account == Account.number,
                        Account.number == accnum,
                    )
                ).order_by(Statement.date).all()

                return jsonify(StatementSchema(many=True).dump(statement_lines))
        except Exception as err:
            raise err
