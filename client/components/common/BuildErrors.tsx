/** @jsx jsx */

import * as React from 'react';
import { jsx, ClassNames } from '@emotion/core';
import { useTheme } from 'emotion-theming';
import { customSet } from 'graphql/fragments/__generated__/customSet';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faExclamationTriangle } from '@fortawesome/free-solid-svg-icons';
import { Popover } from 'antd';
import { useTranslation } from 'i18n';
import { popoverTitleStyle, gold5 } from 'common/mixins';
import { baseStats, scrolledStats, IError } from 'common/types';
import { calcPointCost, renderErrors } from 'common/utils';
import groupBy from 'lodash/groupBy';
import { TTheme } from 'common/themes';

interface IProps {
  customSet: customSet;
  errors: Array<IError>;
  isMobile?: boolean;
}

const BuildErrors: React.FC<IProps> = ({ customSet, errors, isMobile }) => {
  const { t } = useTranslation(['common']);
  const theme = useTheme<TTheme>();

  const groupedErrors = groupBy(errors, ({ reason }) => reason);

  const errorNodes: Array<React.ReactNode> = [];

  Object.entries(groupedErrors).forEach(([reason, arr]) => {
    if (reason === 'CONDITION_NOT_MET') {
      arr.forEach(({ equippedItem, reason }) => {
        errorNodes.push(renderErrors(reason, t, equippedItem, true));
      });
    } else {
      errorNodes.push(renderErrors(reason, t));
    }
  });

  const remainingPoints = baseStats.reduce(
    (acc, statKey) => (acc -= calcPointCost(customSet.stats[statKey], statKey)),
    ((customSet?.level ?? 200) - 1) * 5,
  );

  if (remainingPoints < 0) {
    errorNodes.push(
      <li key="invalid-characteristics">
        {t('INVALID_CHARACTERISTIC_POINTS')}
      </li>,
    );
  }

  scrolledStats.forEach((scrolledStatKey) => {
    if (
      customSet.stats[scrolledStatKey] < 0 ||
      customSet.stats[scrolledStatKey] > 100
    ) {
      errorNodes.push(
        <li key="invalid-scrolled-characteristics">
          {t('INVALID_SCROLLED_CHARACTERISTICS')}
        </li>,
      );
    }
  });

  if (errorNodes.length === 0) {
    return null;
  }

  return isMobile ? (
    <div
      css={{
        marginBottom: 12,
        display: 'flex',
        alignItems: 'flex-start',
        flexDirection: 'column',
        background: theme.layer?.background,
        borderRadius: 4,
        border: `1px solid ${theme.border?.default}`,
        padding: 8,
      }}
    >
      <ul
        css={{
          margin: '0',
          paddingInlineStart: 16,
          fontSize: '0.75rem',
        }}
      >
        {errorNodes}
      </ul>
    </div>
  ) : (
    <div
      css={{
        marginLeft: 20,
        marginTop: 0,
        display: 'flex',
        alignItems: 'center',
      }}
    >
      <ClassNames>
        {({ css }) => (
          <Popover
            title={t('NUM_ERROR', { count: errorNodes.length })}
            content={
              <ul
                css={{ margin: 0, paddingInlineStart: 16, fontSize: '0.75rem' }}
              >
                {errorNodes}
              </ul>
            }
            placement="bottom"
            overlayClassName={css({ ...popoverTitleStyle, maxWidth: 240 })}
          >
            <div>
              <FontAwesomeIcon
                icon={faExclamationTriangle}
                css={{ fontSize: '1.5rem', color: gold5 }}
              />
            </div>
          </Popover>
        )}
      </ClassNames>
    </div>
  );
};

export default BuildErrors;
