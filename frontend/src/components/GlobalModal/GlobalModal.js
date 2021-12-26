import React from "react";
import Modal from "@material-ui/core/Modal";
import Button from "@material-ui/core/Button";
import CloseIcon from "@material-ui/icons/Close";
import "./GlobalModal.css";

export default function GlobalModal({ children, open, onClose, className }) {
  return (
    <div>
      <Modal
        className={className}
        size="lg"
        centered
        open={open}
        onClose={onClose}
      >
        <div>
          <div className="modal__body__area__v2 ar__modal_bodyV2">
            <Button
              className="form__builder__modal__add__close__button"
              variant="secondary"
              onClick={onClose}
            >
              <CloseIcon />
            </Button>
            {children}
          </div>
        </div>
      </Modal>
    </div>
  );
}
